# Health Sqyre Code Assessement

### Setup

Create the virtual environment: 
```
python3 -m venv env
```

Activate the virtual environment:
```
source env/bin/activate
```

Install modules:
```
python -m pip install -r requirements.txt
```

### Running the tests

Be sure to initialize the database before running the tests from the command line:
```
python -m flask init-db
```

Then run the tests with this command:
```
python -m pytest
```
note: use this command vs. `pytest` because it sets the sys.path for relative imports

### Running the app

Like the tests the database needs to be initialized before running. Do that with this command:
```
python -m flask init-db
```

Run the app from the main folder directory (i.e. not the `app` subdirectory):
```
python -m flask run
```

And view the Flask MVC Shopping Cart app by going to localhost:5000 in the web browser!

#### Considerations

1. More testing could be added to the db layer but due to the time constraints of this assignment I kept things as simple as possible.
2. The remove-item and update-quatity endpoints I left as POST methods becasue HTML forms do not support DELETE and PUT so for the purposes of the user interaction with the frontend I made them as such.
