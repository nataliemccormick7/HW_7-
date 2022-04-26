import time

def test_home_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print("\r")
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Welcome to VTM!" in res.data 
        


def test_about_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/mike' route is requested (GET)
    THEN check that the response is valid
    """
    print("-- /mike GET test")
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Vertical Tank Maintenance" in res.data


def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/age' route is requested (GET)
    THEN check that the correct page is displayed
    """
    print("-- /estimate GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Create an estimate" in res.data

def test_estimate_functionality(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the 'future' button is selected (POST)
    THEN check that the correct age is returned to the user
    """
    print("-- /estimate POST test")
    # Functional test - it puts POST data in the age route and looks for the correct value to be returned
    # individual functions to perform the calculations are tested in the Unit tests
    with app.test_client() as test_client:
        # pass in the data use Chrome Developer Tools -> Network -> Click on page -> Payload
        # passing future age value as 'x' because I look for the key(future_age), not the value in app.py if/then stmt
        calc_estimate = {"tank_radius":"180", "tank_height":"360"} 
        res = test_client.post('/estimate', data=calc_estimate)
        assert res.status_code == 200 
        assert b"141300.0" in res.data # may need adjusted depending on current year