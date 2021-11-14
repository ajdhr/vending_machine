# Vending machine

Starting the project:
- create a new virtualenv (Python 3.7.1 interpreter)
- Install requirements with `pip install -r requirements.txt`
- Initialise database with `flask db upgrade` (make sure the sqlite path in DevelopmentConfig is correct for the OS in use)
- Start the application with `flask run` (it should start on http://127.0.0.1:5000/ by default)

Swagger documented APIs are available on http://127.0.0.1:5000/
A postman collection is avilable in "Vending machine.postman_collection.json"

Tests can be run with `python -m unittest discover` 
    