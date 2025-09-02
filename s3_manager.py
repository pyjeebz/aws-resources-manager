import boto3

client = boto3.client('s3')

def list_buckets():
    response = s3.list_buckets()
    print("S3 Buckets: ")
    for bucket in response.get("Buckets", []):
        print(f" - {bucket ['Name']}")

def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket = bucket_name)
        print(f'{bucket_name}' "has been created successfully")

    except Exception as e:
        print("Error creating bucket: {e}")
