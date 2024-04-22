import functions_framework
from googleapiclient.discovery import build

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def launch_dataflow_pipeline(cloud_event):
    """This function will trigger when a file is upload into the rimac-hdd-rawdata bucket.
    """
    data = cloud_event.data
    bucket = data["bucket"]
    name = data["name"]

    if str(data["name"]).endswith(".csv"):
        # Build the Dataflow API client
        service = build('dataflow', 'v1b3')
        project = "analytics-project-373621"  # Replace with your project ID

        template_path = "gs://dataflow-templates-us-east1/latest/GCS_CSV_to_BigQuery"

        template_body = {
            "jobName": "csv2bigquery",
            "environment": {
                "bypassTempDirValidation": False,
                "numWorkers": 2,
                "tempLocation": "gs://rimac-hdd-rawdata/tmp",
                "ipConfiguration": "WORKER_IP_UNSPECIFIED",
                "enableStreamingEngine": False,
                "zone":"us-east1-d",
                "additionalExperiments": [
                    "use_runner_v2"
                ],
                "additionalUserLabels": {}
            },
            "parameters": {
                "inputFilePattern": f"gs://{bucket}/{name}",
                "schemaJSONPath": "gs://rimac-hdd-rawdata/schema/hdd-schema.json",
                "outputTable": "analytics-project-373621:rimac_hdd_dataset.hdd_raw_table",
                "bigQueryLoadingTemporaryDirectory": "gs://rimac-hdd-rawdata/BQ_temp",
                "badRecordsOutputTable": "analytics-project-373621:rimac_hdd_dataset.hdd_raw_error_table",
                "containsHeaders": "true",
                "delimiter": ",",
                "csvFormat": "Default",
                "csvFileEncoding": "UTF-8"
            }
        }

        # Launch the Dataflow pipeline
        request = service.projects().templates().launch(projectId=project, gcsPath=template_path, body=template_body)
        response = request.execute()

        print(response)