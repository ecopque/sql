import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DATABASE_NAME = 'db.sqlite3'
DATABASE_FILE = ROOT_DIR / DATABASE_NAME
TABLE_NAME = 'customers'

var_connection = sqlite3.connect(DATABASE_FILE)
var_cursor = var_connection.cursor()

var_cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)')

var_connection.commit()
var_cursor.close()
var_connection.close()
