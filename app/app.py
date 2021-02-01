import os
from flask import Flask, abort, render_template, redirect, request

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='foo', DATABASE='database.db')

    from . import db   
    from . import forms
    db.init_app(app)

    @app.route('/')
    def main():
        instance = db.get_db()
        items = instance.execute('SELECT * FROM item').fetchall()
        cart_items = instance.execute('SELECT * FROM cart JOIN item ON cart.item_id = item.id').fetchall()
        cart_total = sum(ci[1]*ci[4] for ci in cart_items)
        return render_template('base.html', cart_items=cart_items, cart_total=cart_total, items=items)
    
    @app.route('/add-item', methods=['POST'])
    def add_item():
        form = forms.AddItemForm(request.form, csrf_enabled=False)
        if form.validate():
            instance = db.get_db()
            c = instance.cursor()
            c.execute('INSERT INTO cart (item_id, quantity) VALUES (?, ?)', (form.item.data, form.quantity.data))
            instance.commit()
        else:
            abort(400, 'Form validation failed.')
        return redirect('/')

    @app.route('/remove-item/<int:cart_item_id>', methods=['POST'])
    def remove_item(cart_item_id):
        instance = db.get_db()
        c = instance.cursor()
        c.execute('DELETE FROM cart WHERE item_id=?', (cart_item_id,))
        instance.commit()
        return redirect('/')

    @app.route('/update-quantity/<int:cart_item_id>', methods=['POST'])
    def update_item_quatity(cart_item_id):
        instance = db.get_db()
        c = instance.cursor()
        if request.args.get('action') == 'decrement':
            c.execute('UPDATE cart SET quantity = quantity - 1 WHERE item_id=?', (cart_item_id,))
        elif request.args.get('action') == 'increment':
            c.execute('UPDATE cart SET quantity = quantity + 1 WHERE item_id=?', (cart_item_id,))
        else:
            abort(400, 'action not passed as a query parameter')
        instance.commit()
        return redirect('/')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
