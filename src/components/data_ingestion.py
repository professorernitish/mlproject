import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.exception import CustomException
from src.logger import logging

from src.components.model_trainer import ModelTrainer, ModelTrainingConfig  # Corrected import

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method.")
        try:
            file_path = 'notebook/data/stud.csv'
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File '{file_path}' not found. Please check the path.")
            
            df = pd.read_csv(file_path)
            logging.info("Read the dataset successfully.")

            # Create artifacts directory if not exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Performing train-test split.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully.")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()  # Call once, store returned paths

    # Perform Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data, test_data)

    # Initialize and Train Model
    model_trainer = ModelTrainer()  # Corrected variable name
    r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
    

    print(f"Model Training Completed. R² Score: {r2_score}")

    logging.info("Data transformation and model training completed successfully.")
