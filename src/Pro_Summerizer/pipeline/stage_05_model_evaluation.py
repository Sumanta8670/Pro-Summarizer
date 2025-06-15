from Pro_Summerizer.config.configuration import ConfigurationManager
from Pro_Summerizer.components.model_evaluation import ModelEvaluation
from Pro_Summerizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluation()