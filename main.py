from Pro_Summerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Pro_Summerizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
          logger.exception(e)
          raise e