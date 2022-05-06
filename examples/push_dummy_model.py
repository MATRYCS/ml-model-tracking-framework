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


# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure MLFLow settings to be aware of remote tracker server
mlflow.set_tracking_uri(config.MLFLOW_TRACKING_URI)
mlflow.set_experiment(config.EXPERIMENT_NAME)


def main():
    # Ensure reproducability
    np.random.seed(config.SEED)

    X_train = np.random.random((800, 4))
    y_train = np.full(shape=(800, 1), fill_value=1)

    X_test = np.random.random((200, 4))
    y_test = np.full(shape=(200, 1), fill_value=1)

    model = dummy.DummyRegressor(strategy='constant', constant=1)

    # .start_run() and .end_run() measure time to fit the data.
    # This is more in case of deep learning.
    mlflow.start_run()
    model.fit(X_train, y_train)
    mlflow.end_run()

    # predict values for evaluation
    y_pred = model.predict(X_test)

    # MLFlow will store model into pickle for us.
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path='model',
        registered_model_name=config.REGISTERED_MODEL_NAME, # model registration here or manually on web UI
        pip_requirements=['-r ./requirements.txt'],
    )

    # Log all relevant metrics for given task
    rmse = metrics.mean_squared_error(y_test, y_pred, squared=False)
    mlflow.log_metric('RMSE', rmse)

    mae = metrics.mean_absolute_error(y_test, y_pred)
    mlflow.log_metric('MAE', mae)

    r2 = metrics.r2_score(y_test, y_pred)
    mlflow.log_metric('R2', r2)


    # Plot feature importance, if algorithm supports it.
    if hasattr(model, 'feature_importances_'):
        # get importance
        importance = model.feature_importances_
        fig, ax = plt.subplots()
        # plot feature importance
        ax.bar([x for x in range(len(importance))], importance)

        fig.tight_layout()

        # Store figure into MLFlow
        mlflow.log_figure(fig, artifact_file='feature_importance.png')

    # Plot cumulative distribution function (CDF) of the data
    fig, ax = plt.subplots()
    y_err = np.abs(y_test - y_pred)
    ax.hist(y_err, bins=50, density=True, histtype='step', cumulative=True)
    ax.grid(True)
    ax.set_title('CDF')
    ax.set_xlabel('Estimation error')
    ax.set_ylabel('Likelihood')

    fig.tight_layout()

    # Store figure into MLFlow
    mlflow.log_figure(fig, artifact_file='cdf.png')


if __name__ == "__main__":
    main()

