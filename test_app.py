import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from models import setup_database, Artists, Movies


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        self.token_assistant = os.environ['assistant_token']
        self.token_director = os.environ['director_token']
        self.token_producer = os.environ['producer_token']
        self.actor = {
            "name": "Tom Cruise",
            "age": 50,
            "gender": "male"
        }
        self.movie = {
            "title": "Top Gun",
            "release_date": 1986
        }
        self.app = create_app()
        self.client = self.app.test_client
        setup_database(self.app, self.database_path)
        self.db.drop_all()
        self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    #GET actors success casting asistant
    def test_get_artists_casting_assistant(self):
        res = self.client().get('/Artists', headers={
            "Authorization": 'bearer ' + self.token_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #GET actors failure
    def test_get_artists_no_authorisation(self):
        res = self.client().get('/Artists')
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    #GET movies success casting asistant
    def test_get_movies_casting_assistant(self):
        res = self.client().get('/Movies', headers={
            "Authorization": 'bearer ' + self.token_assistant})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #GET movies failure casting asistant
    def test_get_movies_no_authorisation(self):
        res = self.client().get('/Artists')
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    #GET actor success casting director
    def test_get_actor_casting_director(self):
        #post actor
        res = self.client().post('/Artists', headers={"Authorization": 'bearer ' + self.token_director}, json=self.actor)
        #get actor
        res = self.client().get('/Artists/1', headers={
            "Authorization": 'bearer ' + self.token_director})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertEqual(body['actor'], {'id': 1, 'name': 'Tom Cruise', 'age': 50, 'gender': 'male'})

    #GET actor failure casting director
    def test_get_actor_failure(self):
        res = self.client().get('/Artists/123456789', headers={
            "Authorization": 'bearer ' + self.token_director})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)
        self.assertEqual(body['message'], 'resource not found')

    #GET movie success casting director
    def test_get_movie_casting_director(self):
        #post movie
        res = self.client().post('/Movies', headers={"Authorization": 'bearer ' + self.token_director}, json=self.movie)
        #get movie
        res = self.client().get('/Movies/1', headers={
            "Authorization": 'bearer ' + self.token_director})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)
        self.assertEqual(body['actor'], {'id': 1, 'title': 'Top Gun', 'release_date': 1986})

    #GET movie failure casting director
    def test_get_movie_failure(self):
        res = self.client().get('/Movies/123456789', headers={"Authorization": 'bearer ' + self.token_director})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)
        self.assertEqual(body['message'], 'resource not found')

    #DELETE actor success casting director
    def test_delete_actor_casting_director(self):
        #post actor
        res = self.client().post('/Artists', headers={"Authorization": 'bearer ' + self.token_director}, json=self.actor)
        #delete actor
        res = self.client().delete('/Artists/1', headers={"Authorization": 'bearer ' + self.token_director})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #DELETE actor failure casting asistant
    def test_delete_actor_failure(self):
        res = self.client().delete('/Artists/123456789', headers={"Authorization": 'bearer ' + self.token_director})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)


    #DELETE movie success producer
    def test_delete_movie_casting_director(self):
        #post movie
        res = self.client().post('/Movies', headers={"Authorization": 'bearer ' + self.token_director}, json=self.movie)
        #delete movie
        res = self.client().delete('/Movies/1', headers={"Authorization": 'bearer ' + self.token_director})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #DELETE movie failure casting director
    def test_delete_movie_failure(self):
        res = self.client().delete('/Movies/123456789', headers={"Authorization": 'bearer ' + self.token_producer})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    #POST actors success producer
    def test_post_artist_casting_director(self):
        res = self.client().post('/Artists', headers={"Authorization": 'bearer ' + self.token_director}, json=self.actor)
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #POST actors failure casting asistant
    def test_post_artist_casting_assistant_failure(self):
        res = self.client().post('/Artists', headers={"Authorization": 'bearer ' + self.token_assistant}, json=self.actor)
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    #POST movies success producer
    def test_post_movie_casting_director(self):
        res = self.client().post('/Movies', headers={"Authorization": 'bearer ' + self.token_director}, json=self.movie)
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #POST movies failure casting asistant
    def test_post_movie_casting_assistant_failure(self):
        res = self.client().post('/Movies', headers={"Authorization": 'bearer ' + self.token_assistant}, json=self.movie)
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    #PATCH actor success producer
    def test_patch_artist_casting_director(self):
        #post artist
        res = self.client().post('/Artists', headers={"Authorization": 'bearer ' + self.token_producer}, json=self.actor)
        #patch artist
        res = self.client().patch('Artists/1', headers={"Authorization": 'bearer ' + self.token_producer}, json={'Age': 55})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #PATCH actor failure casting asistant
    def test_patch_artist_casting_assistant_failure(self):
        res = self.client().patch('Artists/1', headers={"Authorization": 'bearer ' + self.token_assistant}, json={'Age': 55})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

    #PATCH movie success producer
    def test_patch_movie_casting_director(self):
        #post movie
        res = self.client().post('/Movies', headers={"Authorization": 'bearer ' + self.token_producer}, json=self.movie)
        #patch movie
        res = self.client().patch('Artists/1', headers={"Authorization": 'bearer ' + self.token_producer}, json={'release_date': 1987})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['success'], True)

    #PATCH movie failure casting asistant
    def test_patch_movie_casting_assistant_failure(self):
        res = self.client().patch('Movies/1', headers={"Authorization": 'bearer ' + self.token_assistant}, json={'Age': 55})
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)

if __name__ == "__main__":
    unittest.main()