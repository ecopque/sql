import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DATABASE_NAME = 'db.sqlite3'
DATABASE_FILE = ROOT_DIR / DATABASE_NAME

var_connection = sqlite3.connect(DATABASE_FILE)
var_cursor = var_connection.cursor()

var_cursor.close()
var_connection.close()
