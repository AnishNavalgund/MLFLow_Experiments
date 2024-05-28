from mlflow.tracking import MlflowClient
from mlflow.entities import ViewType

# Create an MlflowClient instance
client = MlflowClient()

# List all experiments
experiments = client.search_experiments(view_type=ViewType.ACTIVE_ONLY)

# Print details of each experiment
for experiment in experiments:
    print(f"Experiment ID: {experiment.experiment_id}, Name: {experiment.name}")
    
    # Get runs for each experiment
    runs = client.search_runs(experiment_ids=[experiment.experiment_id], run_view_type=ViewType.ACTIVE_ONLY)
    
    # Print details of each run
    for run in runs:
        run_info = run.info
        run_data = run.data
        
        # Run ID and Name
        run_id = run_info.run_id
        run_name = run_data.tags.get("mlflow.runName", "Unnamed run")

        # Artifact Location
        artifact_uri = run_info.artifact_uri
        
        # User ID and Status
        user_id = run_info.user_id
        status = run_info.status
        
        # Start Time and End Time
        start_time = run_info.start_time
        end_time = run_info.end_time
        
        # Source Type and Source Name from Tags
        source_type = run_data.tags.get("mlflow.source.type", "Unknown")
        source_name = run_data.tags.get("mlflow.source.name", "Unknown")
        
        # Parameters
        parameters = run_data.params
        
        # Metrics
        metrics = run_data.metrics
        
        # Tags
        tags = run_data.tags
        
        # Print run details
        print(f"  Run ID: {run_id}, Run Name: {run_name}")
        print(f"    User ID: {user_id}, Status: {status}")
        print(f"    Artifact Location: {artifact_uri}")
        print(f"    Start Time: {start_time}, End Time: {end_time}")
        print(f"    Source Type: {source_type}, Source Name: {source_name}")
        
        # Print Parameters
        print("    Parameters:")
        for param_key, param_value in parameters.items():
            print(f"      {param_key}: {param_value}")
        
        # Print Metrics
        print("    Metrics:")
        for metric_key, metric_value in metrics.items():
            print(f"      {metric_key}: {metric_value}")
        
