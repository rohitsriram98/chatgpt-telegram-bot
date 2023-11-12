import os
from dotenv import load_dotenv
import mysql.connector
import logging

def sqlconn(sqlquery):
    load_dotenv()
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    db_config = {
        "host": os.environ['HOST'],
        "user": os.environ['SQLUSER'],
        "password": os.environ['SQLPASSWORD'],
        "database": os.environ['DATABASE']
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result