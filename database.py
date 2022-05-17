import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


CREATE_TABLE_REGISSEUR = """
CREATE TABLE IF NOT EXISTS regisseur(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL ,
    last_name TEXT NOT NULL,
    is_single INTEGER NOT NULL
    
);
"""

CREATE_TABLE_GENRE = """
CREATE TABLE IF NOT EXISTS genre (
    id INTEGER PRIMARY KEY AUTONINCREMENT,
    name TEXT NOT NULL UNIQUE
    );
"""

CREATE_TABLE_MOVIE = """
CREATE TABLE IF NOT EXISTS movie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL, 
    real_release_date REAL NOT NULL, 
    release_place TEXT NOT NULL,
    duration INTEGER NOT NULL ,
    regisseur_id INTEGER NOT NULL, 
    FOREIGN KEY (regisseur_id) REFERENCES regisseur(id)
    );
"""
INSERT_GENRE = """
INSERT INTO genre (name) VALUES (?)
"""


def create_tables():
    with connection:
        connection.execute(CREATE_TABLE_REGISSEUR)
        connection.execute(CREATE_TABLE_MOVIE)
        connection.execute(CREATE_TABLE_GENRE)

def add_genre(name: str):
    with connection:
        connection.execute(INSERT_GENRE, (name))

def add_entry(name: str):
    with connection:


def create_table():
    connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")

def add_entry(content, date):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?, ?);", (content, date))

def get_entries():
    return connection.execute("SELECT * FROM entries;")