from pyspark.sql.functions import col, upper, current_date

def calculate_age(dob_col):
    from pyspark.sql.functions import datediff
    return (datediff(current_date(), dob_col) / 365).cast("int")

def apply_transformations(df, config):
    rules = config["transformations"]["columns"]

    for rule in rules:
        if rule["transformation"] == "upper":
            df = df.withColumn(rule["target"], upper(col(rule["source"])))

        elif rule["transformation"] == "calculate_age":
            df = df.withColumn(rule["target"], calculate_age(col(rule["source"])))

    return df
