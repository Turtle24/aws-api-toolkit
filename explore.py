import json

from parameters.sagemaker_params import create_algorithm_params

print(json.dumps(create_algorithm_params, indent=4))