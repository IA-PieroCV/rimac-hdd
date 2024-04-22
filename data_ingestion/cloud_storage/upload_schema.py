from google.cloud import storage

# Initialize the client
client = storage.Client()

# Get the bucket
bucket_name = "rimac-hdd-rawdata"
bucket = client.bucket(bucket_name)

# Upload a single file
file_path = "hdd-schema.json"
destination_blob_name = "schema/hdd-schema.json"

blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

print(f"File {file_path} uploaded to {destination_blob_name}.")