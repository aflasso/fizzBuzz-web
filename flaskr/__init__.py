from http import HTTPStatus
import os
from flask import Flask, abort, jsonify, make_response, request


def create_app():
    
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY= 'dev',
        DATABASE = os.path.join(app.instance_path, 'fizzBuzz.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, FizzBuzz!'
    
    @app.route('/fb/<num>', methods=('GET','POST', 'DELETE'))
    def get_fizzBuzz(num):

        return "FizzBuzz", 409
    
    @app.route('/range', methods=('GET','POST', 'DELETE'))
    def range_fizzBuzz():

        return "Range", 404
    
    from . import db
    db.init_app(app)
    
    return app
