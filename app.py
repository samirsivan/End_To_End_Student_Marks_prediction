from src.end_to_end_student_marks_prediction.logger import logging
from src.end_to_end_student_marks_prediction.exception import CustomException
from src.end_to_end_student_marks_prediction.components.data_ingestion import DataIngestion
import sys



if __name__=="__main__":
    myobj = DataIngestion()
    myobj.initiateDataIngestion()
    