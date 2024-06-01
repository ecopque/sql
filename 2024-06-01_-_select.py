import sqlite3
from main import DATABASE_FILE, TABLE_NAME

var_connection = sqlite3.connect(DATABASE_FILE)
var_cursor = var_connection.cursor()

var_cursor.execute(f'SELECT * FROM {TABLE_NAME}')
# var_cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 2') #1:
# var_cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id="3"') #3:

# var_row = var_cursor.fetchone() #2:
# print(var_row) #2:

for in_row in var_cursor.fetchall():
    in_id, in_name, in_weight = in_row
    print(in_id, in_name, in_weight)

var_cursor.close()
var_connection.close()
