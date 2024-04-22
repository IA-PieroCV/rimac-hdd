
from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# Create a new dataset
dataset_id = 'rimac_hdd_dataset'
dataset = bigquery.Dataset(f"{client.project}.{dataset_id}")
dataset.location = "us-east1"
dataset = client.create_dataset(dataset, timeout=30)

# Define the schema for the first table
schema1 = [
    bigquery.SchemaField("Age", "INTEGER"),
    bigquery.SchemaField("Sex", "STRING"),
    bigquery.SchemaField("ChestPainType", "STRING"),
    bigquery.SchemaField("RestingBP", "INTEGER"),
    bigquery.SchemaField("Cholesterol", "INTEGER"),
    bigquery.SchemaField("FastingBS", "INTEGER"),
    bigquery.SchemaField("RestingECG", "STRING"),
    bigquery.SchemaField("MaxHR", "INTEGER"),
    bigquery.SchemaField("ExerciseAngina", "STRING"),
    bigquery.SchemaField("Oldpeak", "FLOAT"),
    bigquery.SchemaField("ST_Slope", "STRING"),
    bigquery.SchemaField("HeartDisease", "INTEGER"),
]

# Create the first table
table_id1 = "hdd_raw_table"
table1 = bigquery.Table(f"{client.project}.{dataset_id}.{table_id1}", schema=schema1)
table1 = client.create_table(table1, exists_ok=True)  # Create the table

# Define the schema for the second table
schema2 = [
    bigquery.SchemaField("RawContent", "STRING"),
    bigquery.SchemaField("ErrorMsg", "STRING"),
]

# Create the second table
table_id2 = "hdd_raw_error_table"
table2 = bigquery.Table(f"{client.project}.{dataset_id}.{table_id2}", schema=schema2)
table2 = client.create_table(table2, exists_ok=True)  # Create the table

print(f"Dataset '{dataset_id}' and tables '{table_id1}' and '{table_id2}' created successfully.")