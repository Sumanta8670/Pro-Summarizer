from  Pro_Summerizer.config.configuration import ConfigurationManager
from Pro_Summerizer.components.model_trainer import ModelTrainer
from Pro_Summerizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()