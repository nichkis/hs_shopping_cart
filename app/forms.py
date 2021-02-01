from wtforms import IntegerField, Form
from wtforms.validators import InputRequired

class AddItemForm(Form):
    quantity = IntegerField('quantity', validators=[InputRequired()])
    item = IntegerField('item', validators=[InputRequired()])

    
