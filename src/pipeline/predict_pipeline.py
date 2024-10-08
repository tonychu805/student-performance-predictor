import sys
import os

import pandas as pd
import numpy as np

from src.exception import CustomException
from src.utils import load_object

import json

class PredictPipeline:

    def __init__(self):

        pass

    def predict(self, features):
        
        try:
            
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            #model_report_path = os.path.join('artifacts','model_report.json')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            #with open(model_report_path, 'r') as f:
            #    model_report = json.load(f)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            print("Before Return")
            preds=model.predict(data_scaled)
            
            return preds
            
        except Exception as e:
        
            raise CustomException(e, sys)         

class CustomData:

    def __init__(self,
                 gender: str,
                 race_ethnicity: str, 
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: float,
                 writing_score: float
                 ):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score




    def get_data_as_data_frame(self):

        try:
            custom_data_input_dict = {
                'gender': [self.gender],
                'race_ethnicity': [self.race_ethnicity], 
                'parental_level_of_education': [self.parental_level_of_education],
                'lunch': [self.lunch],
                'test_preparation_course': [self.test_preparation_course],
                'reading_score': [self.reading_score],
                'writing_score': [self.writing_score]
            }    
        
            return pd.DataFrame(custom_data_input_dict)
    
        except Exception as e:

            raise CustomException(e, sys)
        
