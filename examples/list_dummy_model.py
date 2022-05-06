"""MLFlow can be manipulated through web UI or through code.
Here we show approach through code.

Original: https://www.mlflow.org/docs/latest/model-registry.html#listing-and-searching-mlflow-models
"""
import logging

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn import dummy, metrics
from pprint import pprint

class config:
    MLFLOW_TRACKING_URI = 'http://192.168.0.76:5000/'
    REGISTERED_MODEL_NAME = 'matrycs-dummy-regressor'


def main():
    """Let's retrieve and print some information from MLFlow."""

    client = mlflow.tracking.MlflowClient(
        tracking_uri=config.MLFLOW_TRACKING_URI,
    )

    # Print every registered model
    print('\n\nView all registered models:')
    for mv in client.list_registered_models():
        pprint(dict(mv), indent=4)

    # Retrieve latest releases, if we know registered name.
    print(f'\n\nView latest versions of "{config.REGISTERED_MODEL_NAME}" model:')
    for mv in client.get_latest_versions(name=config.REGISTERED_MODEL_NAME):
        pprint(dict(mv), indent=4)


if __name__ == "__main__":
    main()

