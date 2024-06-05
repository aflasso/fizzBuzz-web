"""
This module contains de data base of the aplication and its configuration
"""
import sqlite3
import uuid
from werkzeug.security import generate_password_hash

import click
from flask import current_app, g
from .Interfaces.i_data_sorage import IdStorage

class DbStorage(IdStorage):
    """
    Class for handling the connection and operations with the database.
    This class provides methods for performing queries and CRUD operations in the database.
    """

    @staticmethod
    def get_db():
        """
        Gets a connection to de database
        """

        if "db" not in g:

            g.db = sqlite3.connect(current_app.config['DATABASE'],
                                   detect_types=sqlite3.PARSE_DECLTYPES)
            g.db.row_factory = sqlite3.Row

        return g.db

    @staticmethod
    def close_bd(e=None):
        """
        Close the connection to de database
        """

        db = g.pop('db', None)

        if db is not None:
            db.close()

    def get_data_by_number(self, data):
        db = DbStorage.get_db()
        query = f"SELECT * FROM fizz_buzz WHERE request == '{data}'"

        result = db.execute(query).fetchone()

        return result

    def get_active_data_by_number(self, data):

        db = DbStorage.get_db()
        query = f"SELECT * FROM fizz_buzz WHERE request == '{data}' AND active = 1"

        result = db.execute(query).fetchone()

        return result

    def post_data(self, data):

        db = DbStorage.get_db()
        query = f"insert into fizz_buzz (request, result) values ('{data.get('number')}','{data.get('result')}')"

        db.execute(query)

        db.commit()

    def update_active_data(self, data):

        db = DbStorage.get_db()
        query = f"UPDATE fizz_buzz SET active = 1 WHERE request = '{data}'"

        db.execute(query)

        db.commit()

    def update_deactive_data(self, data):

        db = DbStorage.get_db()
        query = f"UPDATE fizz_buzz SET active = 0 WHERE request = '{data}'"

        db.execute(query)

        db.commit()

    def get_number_by_range(self, min_value, max_value):

        db = DbStorage.get_db()
        query = f"SELECT * FROM fizz_buzz WHERE CAST(request AS INTEGER) >= {min_value} AND CAST(request AS INTEGER) <= {max_value} AND active = 1 ORDER BY CAST(request AS INTEGER) ASC"

        result = db.execute(query).fetchall()

        return result


def init_bd():
    """
    Initializes the database to its initial state.
    """

    db = DbStorage.get_db()

    with current_app.open_resource('squema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    data = None

    with current_app.open_resource('root.txt') as f:
        data = f.readlines()
        data = [line.decode('utf8').strip() for line in data]

    if data is not None:
        username = data[0]
        password = data[1]

        print(password)

        hashed = generate_password_hash(password, method = 'pbkdf2:sha256')
        db.execute("INSERT INTO user (user, u_password, u_role) VALUES  (?, ?, 1)",
                        (username, hashed))
        db.commit()

@click.command('init-db')
def init_db_command():
    """
    Creates the init-db command application
    """
    init_bd()
    click.echo("Initialized the database.")

def init_app(app):
    """
    Adds the close_db method to every close context,
    adds the init_db_command to the aplication commands
    """

    app.teardown_appcontext(DbStorage.close_bd)
    app.cli.add_command(init_db_command)
