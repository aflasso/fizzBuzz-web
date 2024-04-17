import sqlite3

import click
from flask import current_app, g

def get_db():

    if "db" not in g:

        g.db = sqlite3.connect(current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db

def close_bd(e=None):
    
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_bd():

    db = get_db()

    with current_app.open_resource('squema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    init_bd()
    click.echo("Initialized the database.")

def init_app(app):
    
    app.teardown_appcontext(close_bd)
    app.cli.add_command(init_db_command)