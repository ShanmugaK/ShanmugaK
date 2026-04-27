import json

def read_metadata(pipeline_name):
    with open(f'config/pipeline_config.json') as f:
        pipeline_config = json.load(f)

    with open(f'config/transformation_rules.json') as f:
        transformations = json.load(f)

    return {
        "pipeline": pipeline_config,
        "transformations": transformations
    }
