import mlflow
if  __name__== "__main__":
    #create a new mlflow experiment
        mlflow.create_experiment(
                name="crowd_prediction",
                artifact_location="testing_mlflow_artifacts",
                tags={"env":"mlflowenv","version":"1.0.0"},
        )

