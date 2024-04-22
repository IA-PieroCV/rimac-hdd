from google.cloud import storage

client = storage.Client()
bucket_name = "rimac-hdd-rawdata"
bucket = client.create_bucket(bucket_name)
print(f"Bucket {bucket.name} created.")

bucket = client.bucket(bucket_name)

folder_name = "schema"
blob = bucket.blob(folder_name + "/")
blob.upload_from_string(b'')

print(f"Folder '{folder_name}' created in bucket '{bucket_name}'.")