"""
This module is the main entry point for the Flaskr application.
It contains the configuration, initialization and views of the Flaskr application.
"""
import os
from flask import Flask, abort, jsonify, make_response, request, render_template, flash, redirect, url_for, g
from . import db
from .my_app import MyApp
from flaskr.auth import login_required


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

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/', methods=("GET","POST"))
    @login_required
    def hello():
            

        return render_template("hello.html")

    @app.route('/fb/<num>', methods=('GET','POST', 'DELETE'))
    @login_required
    def get_fizz_buzz(num):

        if request.method == "GET":

            sql_result = system.get_number(num)

            return sql_result
        
        if request.method == "POST":
            sql_result = system.post_number(num)

            return sql_result
        

        if request.method == 'DELETE':

            if g.user["u_role"] == 1:
               print("im admin")
               sql_result = system.delete_hard_number(num)
               return sql_result
            
            sql_result = system.delete_number(num)

            return sql_result

        return "Not Found", 404
    
    
    @app.route('/range', methods=('POST',))
    @login_required
    def range_fizz_buzz():

        request_body = request.json

        min_value = request_body['min']
        max_value = request_body['max']

        if request.method == "POST":
            print("entre")
            sql_result = system.get_range(min_value, max_value)

        return sql_result


    db.init_app(app)

    # app.add_url_rule('/', endpoint="hello")

    return app
