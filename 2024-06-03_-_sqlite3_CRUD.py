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

var_sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'
var_cursor.execute(var_sql, ('Edson', 100))
var_cursor.executemany(var_sql, [('Enéas', 90), ('Carl', 80), ('Baltasar', 70), ('Théo', 60)])
var_connection.commit()

# var_sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name_key, :weight_key)' #1:
# var_cursor.execute(var_sql, {'name_key': 'Enéas', 'weight_key': 100}) #2:
# var_cursor.executemany(var_sql, ({'name_key': 'Carl', 'weight_key': 50}, {'name_key': 'Edson', 'weight_key': 60})) #3:
# var_connection.commit()

var_cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id=1')
var_connection.commit()

var_cursor.execute(f'SELECT * FROM {TABLE_NAME}')
# var_cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 2')
# var_cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id="3"')
var_connection.commit()

for in_row in var_cursor.fetchall():
    in_in, in_name, in_weight = in_row
    print(in_in, in_name, in_weight)

var_cursor.close()
var_connection.close()
