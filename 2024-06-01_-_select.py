import sqlite3
from main import DATABASE_FILE, TABLE_NAME

var_connection = sqlite3.connect(DATABASE_FILE)
var_cursor = var_connection.cursor()

var_cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for in_row in var_cursor.fetchall():
    in_id, in_name, in_weight = in_row
    print(in_id, in_name, in_weight)

var_cursor.close()
var_connection.close()
