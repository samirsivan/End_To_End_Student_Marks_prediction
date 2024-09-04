from src.end_to_end_student_marks_prediction.logger import logging
from src.end_to_end_student_marks_prediction.exception import CustomException
from src.end_to_end_student_marks_prediction.utils import read_sql_data
import sys
import os
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join('artifacts', 'raw.csv')
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    
class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiateDataIngestion(self):
        logging.info("Data Ingestion Started")
        try:
            raw_df = read_sql_data()
            logging.info("Successfully retrievd data from database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            raw_df.to_csv(self.ingestion_config.raw_data_path, header=True, index=False)
            
            train_df, test_df = train_test_split(raw_df, test_size=0.2, random_state=True)
            
            train_df.to_csv(self.ingestion_config.train_data_path, header=True, index=False)
            test_df.to_csv(self.ingestion_config.test_data_path, header=True, index=False)
            logging.info("DataIngestion Completed")
        except Exception as e:
            logging.info("Something went wrong with initiateDataIngestion function from DataIngestion class")
            raise CustomException(e, sys)