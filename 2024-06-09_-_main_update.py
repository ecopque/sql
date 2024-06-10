# pip install pymysql
# pip install python-dotenv
# pip install types-pymysql

import pymysql #1:
import dotenv #2:
import os #3:

TABLE_NAME = 'customers' #14:
dotenv.load_dotenv() #4:

var_connection = pymysql.connect(host=os.environ['MYSQL_HOST'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'], database=os.environ['MYSQL_DATABASE'], charset='utf8mb4') #5:
var_cursor = var_connection.cursor() #6:

print(os.environ['MYSQL_DATABASE']) #7: #8:

with var_connection: #9:
    with var_connection.cursor() as var_cursor: #10:
        var_cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))') #13:
        var_cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}') #15:
        var_connection.commit()
        print(var_cursor)
    print()
    with var_connection.cursor() as var_cursor: #16:
        var_sql = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)'
        
        var_data1 = ('Edson', 100)
        var_result = var_cursor.execute(var_sql, var_data1)

        var_data2 = (('Carl', 120), ('Enéas', 150))
        var_resul2 = var_cursor.executemany(var_sql, var_data2)
        
        var_connection.commit()
        print(var_sql, var_data1)
        print(var_sql, var_data2)
    print()
    with var_connection.cursor() as var_cursor:
        var_sql = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s , %(age)s)'

        var_data3 = {'name':'Gracian', 'age':125}
        var_resul3 = var_cursor.execute(var_sql, var_data3)

        var_connection.commit()
        print(var_sql, var_data3)
    print()
    with var_connection.cursor() as var_cursor:
        var_sql =  f'SELECT id, age FROM {TABLE_NAME}'
        var_cursor.execute(var_sql)

        var_data_one = var_cursor.fetchone()
        print(var_data_one) #AAA:
    print()
    with var_connection.cursor() as var_cursor:
        var_sql = f'SELECT * FROM {TABLE_NAME}'
        var_cursor.execute(var_sql)

        var_data_all = var_cursor.fetchall()
        for var_row in var_data_all:
            print(var_row) #BBB:
    print()
    with var_connection.cursor() as var_cursor:
        var_sql = f'SELECT * FROM {TABLE_NAME} WHERE id >= 3'
        var_cursor.execute(var_sql)
        var_data = var_cursor.fetchall()
        var_connection.commit()
        print(var_cursor.mogrify(var_sql)) #DDD:

        for var_row in var_data:
            print(var_row) #CCC:
    print()
    with var_connection.cursor() as var_cursor:
        var_input = input('Type an id: ')
        var_id = 'id'
        try:
            var_input = int(var_input)
            var_sql = f'SELECT * FROM {TABLE_NAME} WHERE {var_id} > %s'
            var_cursor.execute(var_sql, (var_input,))
            var_data = var_cursor.fetchall()

            for var_row in var_data:
                print(var_row)
        except ValueError:
            print("Please enter a valid integer for the id.")
    print()
    with var_connection.cursor() as var_cursor:
        var_input_smaller = input('Type an smaller id: ')
        var_input_bigger = input('Type an bigger id: ')
        var_id = 'id'
        try:
            var_input_smaller = int(var_input_smaller)
            var_input_bigger = int(var_input_bigger)
            var_sql = f'SELECT * FROM {TABLE_NAME} WHERE {var_id} >= %s AND {var_id} <= %s' # BETWEEN %S AND %S
            var_cursor.execute(var_sql, (var_input_smaller, var_input_bigger))
            var_data = var_cursor.fetchall()

            for var_row in var_data:
                print(var_row)
        except ValueError:
            print('xxx')
    print()

    with var_connection.cursor() as var_cursor:
        var_sql_update = f'UPDATE {TABLE_NAME} SET name=%s, age=%s WHERE id=%s'
        var_cursor.execute(var_sql_update, ('Rufa', 160, 3,))
        var_connection.commit()

        var_sql_select = f'SELECT * FROM {TABLE_NAME}'
        var_cursor.execute(var_sql_select)
        var_data = var_cursor.fetchall()

        for var_row in var_data:
            print(var_row)

    print()
    with var_connection.cursor() as var_cursor:
        var_sql_delete = f'DELETE FROM {TABLE_NAME} WHERE id = %s'
        var_cursor.execute(var_sql_delete, (3,))
        var_connection.commit()

        var_sql_select = f'SELECT * FROM {TABLE_NAME}'
        var_cursor.execute(var_sql_select)
        var_data = var_cursor.fetchall()
        for var_row in var_data:
            print(var_row)

# var_cursor.close() #11:
# var_connection.close() #12:
