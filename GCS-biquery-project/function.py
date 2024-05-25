# from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    # service = build('dataflow', 'v1b3')
    project = "dulcet-yew-424213-u6"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
    "jobName": "bq-load",  # Provide a unique name for the job
    "parameters": {
        "inputFilePattern": "gs://project-gcs-bigquery/user_data.csv",
        "JSONPath": "gs://project-gcs-bigquery-metadata/bq.json",
        "outputTable": "dulcet-yew-424213-u6:project_gsc_bq.users",
        "bigQueryLoadingTemporaryDirectory": "gs://project-gcs-bigquery-metadata",
        "javascriptTextTransformGcsPath": "gs://project-gcs-bigquery-metadata/udf.js",
        "javascriptTextTransformFunctionName": "transform",
        
    }
    }
    

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)