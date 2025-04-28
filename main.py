from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)

stage_Name = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {stage_Name} started<<<<<<<<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()

    data_ingestion.main()
    logger.info(f">>>>>>> stage {stage_Name} completed<<<<<<<<<\n x=================x")

except Exception as e:
    logger.exception(e)
    raise e


stage_Name = "Prepare base model"
try:
    logger.info(f">>>>>> stage {stage_Name} started<<<<<<<<<<<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()

    prepare_base_model.main()
    logger.info(f">>>>>>> stage {stage_Name} completed<<<<<<<<<\n x=================x")

except Exception as e:
    logger.exception(e)
    raise e
