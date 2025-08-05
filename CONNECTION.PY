# db_connection.py
import sqlite3

def connect_db():
    return sqlite3.connect("movie1.db")
