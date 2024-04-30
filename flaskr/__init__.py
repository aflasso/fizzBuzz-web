"""
This module is the main entry point for the Flaskr application.
It contains the configuration, initialization and views of the Flaskr application.
"""
import os
from flask import Flask, abort, jsonify, make_response, request
from . import db
from .my_app import MyApp


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        app (Flask): The configured Flask application.
    """

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
    def get_fizz_buzz(num):

        if request.method == "GET":

            sql_result = system.get_number(num)
            return sql_result

        if request.method == "POST":

            sql_result = system.post_number(num)
            return sql_result

        if request.method == 'DELETE':
            sql_result = system.delete_number(num)
            return sql_result

        return "Not Found", 404

    @app.route('/range', methods=('POST',))
    def range_fizz_buzz():

        request_body = request.json

        min_value = request_body['min']
        max_value = request_body['max']

        if request.method == "POST":
            print("entre")
            sql_result = system.get_range(min_value, max_value)

        return sql_result


    db.init_app(app)

    return app
