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
    
    with var_connection.cursor() as var_cursor: #16:
        var_sql = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)'
        
        var_data1 = ('Edson', 100)
        var_result = var_cursor.execute(var_sql, var_data1)

        var_data2 = (('Carl', 120), ('Enéas', 150))
        var_resul2 = var_cursor.executemany(var_sql, var_data2)
        
        var_connection.commit()
        print(var_sql, var_data1)
        print(var_sql, var_data2)

    with var_connection.cursor() as var_cursor:
        var_sql = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s , %(age)s)'

        var_data3 = {'name': 'Gracian', 'age': 125}
        var_resul3 = var_cursor.execute(var_sql, var_data3)

        var_connection.commit()
        print(var_sql, var_data3)

    with var_connection.cursor() as var_cursor:
        var_sql =  f'SELECT id, age FROM {TABLE_NAME}'
        var_cursor.execute(var_sql)

        var_data_one = var_cursor.fetchone()
        print(var_data_one) #AAA:

    with var_connection.cursor() as var_cursor:
        var_sql = f'SELECT * FROM {TABLE_NAME}'
        var_cursor.execute(var_sql)

        var_data_all = var_cursor.fetchall()
        for var_row in var_data_all:
            print(var_row) #BBB:

    with var_connection.cursor() as var_cursor:
        var_sql = f'SELECT * FROM {TABLE_NAME} WHERE id = 3'
        var_cursor.execute(var_sql)
        var_data = var_cursor.fetchall()
        var_connection.commit()

        for var_row in var_data:
            print(var_row)

       
# var_cursor.close() #11:
# var_connection.close() #12:
