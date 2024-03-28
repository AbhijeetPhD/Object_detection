import os
import sys
from signLanguage.constant.training_pipeline import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = os.path.join(ARTIFACTS_DIR,TIMESTAMP)

training_pipeline_config: TrainingPipelineConfig= TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:

    data_ingestion_dir:str = os.path.join(training_pipeline_config.artifacts_dir,DATA_INGESTION_DIR_NAME)

    features_store_path:str = os.path.join(data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR)

    data_download_url:str = DATA_DOWNLOAD_URL

@dataclass

class DataValidationConfig:

    data_validation_dir:str= os.path.join(training_pipeline_config.artifacts_dir,DATA_VALIDATION_DIR_NAME)
    data_valid_dir:str= os.path.join(data_validation_dir,DATA_VALIDATION_STATUS_FILE)
    data_val_required_list=DATA_VALIDATION_ALL_REQUIRED_FILES


@dataclass

class ModelTrainerConfig:
    model_trainer_dir:str=os.path.join(training_pipeline_config.artifacts_dir,MODEL_TRAINER_DIR_NAME)
    
    weight_name=MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    
    no_epochs=MODEL_TRAINER_NO_EPOCH
    
    batch_size=MODEL_TRAINER_BATCH_SIZE




    






