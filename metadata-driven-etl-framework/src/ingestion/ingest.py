def ingest_data(config):
    source_table = config["pipeline"]["source"]
    return spark.read.table(source_table)
