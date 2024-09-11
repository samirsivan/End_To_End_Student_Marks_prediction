from src.end_to_end_student_marks_prediction.exception import CustomException
from src.end_to_end_student_marks_prediction.logger import logging
import os
import sys
from pandas import DataFrame
from typing import List
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_file_path:str = os.path.join('artifacts', 'preprocessor.joblib')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()
        
    def get_preprocessor_obj(self):
        '''
            this function returns the preprocessor object for data transformation
        '''
        try:
            logging.info("Starting to get preprocessor obj")
            
        except Exception as e:
            logging.info("Something went wrong while retrieving the preprocessor obj")
            raise CustomException(e, sys)