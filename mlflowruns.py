import mlflow

if __name__ == "__main__":
    # Start an MLflow run
    with mlflow.start_run(run_name=("detection rate")):
        # Your machine learning code goes here

        # Example: Log a parameter
        mlflow.log_param("detection_rate", 0.01)

    # The MLflow run ends automatically when you exit the 'with' block

