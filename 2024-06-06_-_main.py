# pip install pymysql
# pip install python-dotenv
# pip install types-pymysql

import pymysql
import dotenv
import os

dotenv.load_dotenv()

var_connection = pymysql.connect(host=os.environ['MYSQL_HOST'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'], database=os.environ['MYSQL_DATABASE'])
var_cursor = var_connection.cursor()

print(os.environ['MYSQL_DATABASE'])

with var_connection:
    with var_connection.cursor() as cursor:
        print(cursor)
    
# var_cursor.close()
# var_connection.close()
