from framework.metadata_reader import read_metadata
from ingestion.ingest import ingest_data
from transformation.transform import apply_transformations
from load.load import load_data

def run_pipeline(pipeline_name):
    config = read_metadata(pipeline_name)

    df = ingest_data(config)
    df_transformed = apply_transformations(df, config)
    load_data(df_transformed, config)

if __name__ == "__main__":
    run_pipeline("customer_etl")
