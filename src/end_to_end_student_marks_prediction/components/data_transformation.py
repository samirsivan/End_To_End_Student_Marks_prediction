from src.end_to_end_student_marks_prediction.exception import CustomException
from src.end_to_end_student_marks_prediction.logger import logging
import os
import sys
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from typing import List
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_file_path:str = os.path.join('artifacts', 'preprocessor.joblib')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()
        
    def get_preprocessor_obj(self, num_cols:List[str], cat_cols:List[str]):
        '''
            this function returns the preprocessor object for data transformation
        '''
        try:
            logging.info("Starting to get preprocessor obj")
            
            num_pipeline = Pipeline(steps=[
                ('num_imputer', SimpleImputer(strategy='median')),
                ('scale', StandardScaler())
            ])
            
            cat_pipeline = Pipeline(steps=[
                ('cat_imputer', SimpleImputer(strategy='most_frequent')),
                ('ohe', OneHotEncoder(drop='first', handle_unknown='ignore'))
            ])
            
            preprocessor_obj = ColumnTransformer(transformers=[
                ('num_pipeline', num_pipeline, num_cols),
                ('cat_pipeline', cat_pipeline, cat_cols)
            ], remainder='passthrough')
            
            return preprocessor_obj
            
        except Exception as e:
            logging.info("Something went wrong while retrieving the preprocessor obj")
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path:str, test_path:str):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading Train & Test Data")
            target_col = 'math_score'
            
            X_train = train_df.drop(columns=[target_col], axis=1)
            y_train = train_df[target_col]
            
            X_test = test_df.drop(columns=[target_col], axis=1)
            y_test = test_df[target_col]
            
            num_cols = X_train.select_dtypes(include=np.number).columns
            cat_cols = X_train.select_dtypes(exclude=np.number).columns
        
            preprocessor_obj = self.get_preprocessor_obj(num_cols=num_cols, cat_cols=cat_cols)
            
            logging.info("Successfully got preprocessor object")
            
        except Exception as e:
            raise CustomException(e, sys)
        
        