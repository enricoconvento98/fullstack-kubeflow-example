import kfp
from kfp import dsl
from kfp.components import func_to_container_op

@func_to_container_op
def log_to_backend(run_id: str, metrics: dict):
    import requests
    import json
    
    try:
        requests.post(
            "http://backend:8000/api/runs",
            json={"run_id": run_id, "status": "completed"}
        )
        
        for name, value in metrics.items():
            requests.post(
                "http://backend:8000/api/metrics",
                json={
                    "run_id": run_id,
                    "metric_name": name,
                    "metric_value": value
                }
            )
    except Exception as e:
        print(f"Failed to log to backend: {str(e)}")

@dsl.pipeline(name='fullstack-ml-pipeline')
def fullstack_pipeline():
    # Your pipeline steps would go here
    # For development, we'll just log test metrics
    log_to_backend(
        run_id=dsl.RUN_ID_PLACEHOLDER,
        metrics={"accuracy": 0.95, "f1": 0.92}
    )