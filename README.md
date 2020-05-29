# Casting Agency API

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Getting Started

### Installing Dependencies

#### Python 3.8.2

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It is recommened to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

First ensure that you are working in the created virtual environment.

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=api.py
export FLASK_ENV=development
flask run
```

Sourcing setup.sh sets some environment variables used by the app.

Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to api.py directs flask to use the this file to find the application.

You can run this API locally at the default http://127.0.0.1:5000/

## Testing

```bash
dropdb castingAgency
createdb castingAgency
python test_app.py
```

## Deployment

Application is hosted on Heroku: https://casting-agency-fsnd-przemek89.herokuapp.com/

## API Reference

### Getting Started

- Base URL: https://casting-agency-fsnd-przemek89.herokuapp.com/
- Authentication: This app has got 3 users. Each has his own token which are provided in setup.sh file. Details about each user privilege are provided below.

### Endpoints

- GET '/Artists'
- GET '/Artists/<int:artist_id>'
- GET '/Movies'
- GET '/Movies/<int:movie_id>'
- DELETE '/Artists/<int:artist_id>'
- DELETE '/Movies/<int:movie_id>'
- POST '/Artists'
- POST '/Movies'
- PATCH '/Artists/<int:artist_id>'
- PATCH '/Movies/<int:movie_id>'

Below

#### GET Artists

GET '/Artists'
- Request Arguments: None
- Returns a list of Artists
- Sample:
```python
{'artists' : [
    {'name': 'Tom Cruise',
    'age': 50,
    'gender': 'male'}
    ]}
```

#### GET Artist
#### GET Movies
#### GET Movie
#### DELETE Artist
#### DELETE Movie
#### POST Artists
#### POST Movies
#### PATCH Artist
#### PATCH Movie

### Users

This app has 3 users. each user has his own privileges.
- Casting Assistant
    - Can view actors and movies
- Casting Director
    - All permissions of a Casting Assistant and…
    - Add or delete an actor from the database
    - Modify actors or movies
- Executive Producer
    - All permissions of a Casting Director and…
    - Add or delete a movie from the database

### Environment Variables

In the setup.sh file there are JWT tokens for each User Role

- CASTING_ASSISTANT
- CASTING_DIRECTOR
- EXECUTIVE_PRODUCER
