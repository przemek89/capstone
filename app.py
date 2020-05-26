import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_database, Artists, Movies

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_database(app)
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
    return response

# GET /artists'
  @app.route('/artists', methods=['GET'])
  def get_all_actors():
    artists_query = Artists.query.all()
    artists = [artist.format() for artist in artists_query]

    if artists_query is None:
      abort(404)
    else:
      return jsonify({
        'success': True,
        'artists': artists
      })

# GET /artists/<int:artist_id>
  @app.route('/artists/<int:artist_id>', methods=['GET'])
  def get_actor(artist_id):
    artist = Artists.query.get(artist_id)
    if artist is None:
      abort(404)
    else:
      artist = artist.format()
      return jsonify({
        'success': True,
        'artist': artist
      })

# GET movies
  @app.route('/movies', methods=['GET'])
  def get_all_movies():
    movies_query = Movies.query.all()
    movies = [movie.format() for movie in movies_query]

    if movies_query is None:
      abort(404)
    else:
      return jsonify({
        'success': True,
        'movies': movies
      })

# GET movies/id
  @app.route('/movies/<int:movie_id>', methods=['GET'])
  def get_movie(movie_id):
    movie = Movies.query.get(movie_id)
    if movie is None:
      abort(404)
    else:
      movie = movie.format()
      return jsonify({
        'success': True,
        'movie': movie
      })

# DELETE artist/id
  @app.route('/artists/<int:artist_id>', methods=['DELETE'])
  def delete_artist(artist_id):
    try:
      artist_to_be_deleted = Artists.query.filter_by(id=artist_id).one_or_none()
      if artist_to_be_deleted is None:
        abort(404)
      else:
        deleted_artist_id = artist_to_be_deleted.id
        artist_to_be_deleted.delete()
    except:
      abort(422)
    return jsonify({
      'success': True,
      'deleted_artist_id': deleted_artist_id
    })

# DELETE movies/id
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  def delete_movie(movie_id):
    try:
      movie_to_be_deleted = Movies.query.filter_by(id=movie_id).one_or_none()
      if movie_to_be_deleted is None:
        abort(404)
      else:
        deleted_movie_id = movie_to_be_deleted.id
        movie_to_be_deleted.delete()
    except:
      abort(422)
    return jsonify({
      'success': True,
      'deleted_artist_id': deleted_movie_id
    })

# POST actors
# POST movies
# PATCH actors/id
# PATCH movies/id
# 404 error
# 422 error

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)