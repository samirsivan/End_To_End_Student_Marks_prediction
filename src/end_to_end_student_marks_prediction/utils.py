from src.end_to_end_student_marks_prediction.logger import logging
from src.end_to_end_student_marks_prediction.exception import CustomException
import sys
import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("user")
host = os.getenv("host")
password = os.getenv("password")
dbname = os.getenv("dbname")

def read_sql_data():
    try:
        mydb = psycopg2.connect(
            user= user,
            host= host,
            password = password,
            dbname = dbname
        )
        logging.info("Connection Successfully Established")
        query = "Select * from student_performance"
        df = pd.read_sql_query(query, mydb)
    except Exception as e:
        logging.info("Connection was unsuccessfull")
        raise CustomException(e, sys)
    
    finally:
        if mydb:
            mydb.close()
            
    return df