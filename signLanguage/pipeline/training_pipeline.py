import os,sys
from signLanguage.constant.training_pipeline import *
from signLanguage.entity.config_entity import (DataIngestionConfig,
                                               DataValidationConfig,
                                               ModelTrainerConfig)
from signLanguage.entity.artifacts_entity import (DataIngestionArtifact,
                                                   DataValidationArtifact,
                                                   ModelTrainerArtifact)

from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer
from signLanguage.logger import logging
from signLanguage.exception import SignException



class TrainPipeline:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        self.validation_config=DataValidationConfig()
        self.model_trainer_config=ModelTrainerConfig()
    



    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from URL")
            data_ingestion=DataIngestion(data_ingestion_config=self.ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()

            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e,sys)

    
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:

            data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                            data_validation_config=self.validation_config)

            data_validation_artifact=data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise SignException(e,sys)

    def start_model_trainer(self)->ModelTrainerArtifact:

        try:
            model_trainer=ModelTrainer(model_trainer_config=self.model_trainer_config)
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        
        except Exception as e:
            raise SignException(e,sys)
           

    
    def run_pipeline(self)->None:

        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            

            if data_validation_artifact.data_validation_status==True:
                 model_trainer_artifact=self.start_model_trainer()

            else:
                raise Exception("data is not in proper format")


        except Exception as e:
            raise SignException(e,sys)






