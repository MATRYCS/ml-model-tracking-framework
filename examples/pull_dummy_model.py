"""This example will pull latest model marked as "Production" version."""
import logging

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn import dummy, metrics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class config:
    SEED = 42
    MLFLOW_TRACKING_URI = 'http://192.168.0.76:5000/'
    EXPERIMENT_NAME = 'dummy-regression'
    REGISTERED_MODEL_NAME = 'matrycs-dummy-regressor'

    STAGE = 'Production'


# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure MLFLow settings to be aware of remote tracker server
mlflow.set_tracking_uri(config.MLFLOW_TRACKING_URI)

def main():
    model = mlflow.pyfunc.load_model(
        model_uri=f'models:/{config.REGISTERED_MODEL_NAME}/{config.STAGE}',
        suppress_warnings=False,
    )

    # Retrieve the data
    N_SAMPLES = 2
    N_FEATURES = 4  # 'matrycs-dummy-regressor' accepts 4 inputs

    input_size = (N_SAMPLES, N_FEATURES) 
    inputs = np.random.random(input_size)

    outputs = model.predict(inputs)
    print(f'Model output for {N_SAMPLES} sample(s):\n\t{outputs}')



if __name__ == "__main__":
    main()

