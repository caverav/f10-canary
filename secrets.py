"""Synthetic credentials sample for the analysis path."""
import sqlite3

AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def lookup(conn: sqlite3.Connection, name: str):
    """Query built by concatenation, for the analyzer to catch."""
    return conn.execute("SELECT * FROM users WHERE name = '" + name + "'").fetchall()
