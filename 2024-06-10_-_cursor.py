import pymysql
import pymysql.cursors
import dotenv
import os

TABLE_NAME = 'customers'
dotenv.load_dotenv() #11:

var_connection = pymysql.connect(host=os.environ['MYSQL_HOST'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'], database=os.environ['MYSQL_DATABASE'], charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor) #12:

var_cursor = var_connection.cursor()

with var_connection:
    with var_connection.cursor() as var_cursor:
        var_cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))')
        var_cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}') #13:
        var_connection.commit()

    with var_connection.cursor() as var_cursor:
        var_sql_insert = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)'
        
        var_data1 = ('Edson', 100)
        var_result = var_cursor.execute(var_sql_insert, var_data1)
        var_data2 = (('Carl', 120), ('Enéas', 150))
        var_resul2 = var_cursor.executemany(var_sql_insert, var_data2)
        var_connection.commit()
        
        var_sql_select = f'SELECT * FROM {TABLE_NAME}'
        var_cursor.execute(var_sql_select)

        var_data = var_cursor.fetchall() #15:
        var_connection.commit() #14:
        
        print()
        for var_row in var_data:
            print(var_row) #1:

        print()
        for var_row in var_data:
            print(var_row['name']) #2: #16:

        print()
        var_cursor.scroll(-2) #17:
        # var_cursor.scroll(1)
        for var_row in var_cursor.fetchall(): #18:
            print(var_row) #3:
        
        print()
        var_cursor.scroll(2, 'absolute') #19:
        for var_row in var_cursor.fetchall(): #20:
            print(var_row) #4:

        print()
        var_sql_insert = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)'
        var_data3 = ('Théo', 110)
        var_cursor.execute(var_sql_insert, var_data3)
        var_connection.commit()

        var_sql_select = f'SELECT * FROM {TABLE_NAME}'
        var_cursor.execute(var_sql_select)
        var_data4 = var_cursor.fetchall()
        var_connection.commit()
        
        print('len(var_data):', len(var_data)) #5: #22:
        print('len(var_data4):', len(var_data4)) #8: #23:
        print('var_cursor.rowcount:', var_cursor.rowcount) #6: #21:

        print()
        print('rownumber', var_cursor.rownumber) #10:

        print()
        var_data5 = ('Michigan', 300)
        var_cursor.execute(var_sql_insert, var_data5)
        var_connection.commit()
        print('var_cursor.lastrowid:', var_cursor.lastrowid) #7: #24:

        print()
        var_cursor.execute(f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1')
        var_last_id_select = var_cursor.fetchone()
        print('var_last_id_select:', var_last_id_select) #9:

        # var_data = var_cursor.fetchall()
        # print('var_sql_inser: ', len(var_data))
