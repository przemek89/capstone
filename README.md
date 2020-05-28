# Casting

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

## Deployment

## API Reference

### Getting Started

### Endpoints

## GET Artists
## GET Artist
## GET Movies
## GET Movie
## DELETE Artist
## DELETE Movie
## POST Artists
## POST Movies
## PATCH Artist
## PATCH Movie

### Users