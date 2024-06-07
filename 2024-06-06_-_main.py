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
    with var_connection.cursor() as cursor: #10:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))') #13:
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}') #15:
        var_connection.commit()
        print(cursor)
    
    with var_connection.cursor() as cursor: #16:
        var_result = cursor.execute(f'INSERT INTO {TABLE_NAME} (name, age) VALUES ("Edson", 100)') #17:
        var_resul2 = cursor.execute(f'INSERT INTO {TABLE_NAME} (name, age) VALUES ("Carl", 100), ("Enéas", 150)') #17:
        print(var_result)
        var_connection.commit()

# var_cursor.close() #11:
# var_connection.close() #12:
