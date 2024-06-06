# pip install pymysql
# pip install python-dotenv
# pip install types-pymysql

import pymysql #1:
import dotenv #2:
import os #3:

dotenv.load_dotenv() #4:

var_connection = pymysql.connect(host=os.environ['MYSQL_HOST'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'], database=os.environ['MYSQL_DATABASE']) #5:
var_cursor = var_connection.cursor() #6:

print(os.environ['MYSQL_DATABASE']) #7: #8:

with var_connection: #9:
    with var_connection.cursor() as cursor: #10:
        cursor.execute('CREATE TABLE IF NOT EXISTS customers (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))')
        var_connection.commit()
        print(cursor)
    
# var_cursor.close() #11:
# var_connection.close() #12:
