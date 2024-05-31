import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DATABASE_NAME = 'db.sqlite3'
DATABASE_FILE = ROOT_DIR / DATABASE_NAME
TABLE_NAME = 'customers'

var_connection = sqlite3.connect(DATABASE_FILE)
var_cursor = var_connection.cursor()

var_cursor.execute(f'DELETE FROM {TABLE_NAME}')
var_cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
var_connection.commit()

var_cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)')
var_connection.commit()

var_sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name_key, :weight_key)' #1:
var_cursor.execute(var_sql, {'name_key': 'Enéas', 'weight_key': 100}) #2:
var_cursor.executemany(var_sql, ({'name_key': 'Carl', 'weight_key': 50}, {'name_key': 'Edson', 'weight_key': 60})) #3:
var_connection.commit()

var_cursor.close()
var_connection.close()
