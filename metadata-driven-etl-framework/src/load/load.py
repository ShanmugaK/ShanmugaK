def load_data(df, config):
    target = config["pipeline"]["target"]
    load_type = config["pipeline"]["load_type"]

    if load_type == "full":
        df.write.mode("overwrite").saveAsTable(target)

    elif load_type == "incremental":
        df.createOrReplaceTempView("staging")

        merge_sql = f"""
        MERGE INTO {target} t
        USING staging s
        ON t.customer_id = s.customer_id
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED THEN INSERT *
        """

        spark.sql(merge_sql)
