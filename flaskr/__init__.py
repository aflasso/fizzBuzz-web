from http import HTTPStatus
import os
from flask import Flask, abort, jsonify, make_response, request

from .my_app import MyApp


def create_app():
    
    app = Flask(__name__, instance_relative_config=True)

    system = MyApp()

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

        if request.method == "GET":

            result = system.get_active_number(num)

            return result
        
        if request.method == "POST":

            sql_result = system.post_number(num)
            return sql_result

        
    
    @app.route('/range', methods=('GET','POST', 'DELETE'))
    def range_fizzBuzz():

        return "Range", 404
    
    from . import db
    db.init_app(app)
    
    return app
