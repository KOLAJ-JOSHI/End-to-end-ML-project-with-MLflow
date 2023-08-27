from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import STAGE_NAME, DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx=======================x")
except Exception as e:
    logger.exception(e)
    raise e