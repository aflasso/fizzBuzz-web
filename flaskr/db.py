import sqlite3

import click
from flask import current_app, g
from .Interfaces.i_data_sorage import IdStorage

class DbStorage(IdStorage):

    @staticmethod
    def get_db():

        if "db" not in g:

            g.db = sqlite3.connect(current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
            g.db.row_factory = sqlite3.Row

        return g.db

    @staticmethod
    def close_bd(e=None):
        
        db = g.pop('db', None)

        if db is not None:
            db.close()
    
    def get_data_by_number(self, data) -> any:
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

        return 
    
    def update_active_data(self, number):

        db = DbStorage.get_db()
        query = f"UPDATE fizz_buzz SET active = 1 WHERE request = '{number}'"

        db.execute(query)

        db.commit()
        return 
    
    def update_deactive_data(self, number):

        db = DbStorage.get_db()
        query = f"UPDATE fizz_buzz SET active = 0 WHERE request = '{number}'"

        db.execute(query)

        db.commit()
        return 
    
    def get_number_by_range(self, min_value, max_value):
        
        db = DbStorage.get_db()
        query = f"SELECT * FROM fizz_buzz WHERE CAST(request AS INTEGER) >= {min_value} AND CAST(request AS INTEGER) <= {max_value} AND active = 1 ORDER BY CAST(request AS INTEGER) ASC"

        result = db.execute(query).fetchall()

        return result


def init_bd():

    db = DbStorage.get_db()

    with current_app.open_resource('squema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    init_bd()
    click.echo("Initialized the database.")

def init_app(app):
    
    app.teardown_appcontext(DbStorage.close_bd)
    app.cli.add_command(init_db_command)