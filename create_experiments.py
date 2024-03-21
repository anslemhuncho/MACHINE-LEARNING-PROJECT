import mlflow
#create a new mlflow experiment 
if __name__ == "__main__":
    mlflow.create_experiment(
        name="crowd_prediction_experiment",
        artifact_location="crowd_predition_experiment_artifacts",
        tags={"env":"mlflowenv","version":"1.0.0"}
    )
    