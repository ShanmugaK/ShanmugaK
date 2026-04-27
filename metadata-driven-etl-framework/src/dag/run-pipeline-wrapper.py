import logging

def run_pipeline_wrapper(pipeline_name):
    try:
        logging.info(f"Starting pipeline: {pipeline_name}")
        run_pipeline(pipeline_name)
        logging.info(f"Completed pipeline: {pipeline_name}")
    except Exception as e:
        logging.error(f"Pipeline failed: {pipeline_name} | Error: {str(e)}")
        raise
