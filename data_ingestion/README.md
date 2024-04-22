# Data Ingestion step (Out of scope)
The data ingestion step is the first step to make here. The roles involved are data analyst. There are three resources involved:
- Cloud storage: We used a bucket to save raw data.
- Bigquery: We used a Bigquery dataset to save the raw data into tables and make it available to all the data science team.
- Cloud Function: We use a Cloud Function to trigger a Dataflow pipeline to check the CSV integrity and load the data into the Bigquery Table.