import boto3

client = boto3.client('ec2')

def list_instance():
    response = client.describe_instances()
    print("Raw response:", response)  # Debug line
    print("EC2 instance(s) created:")
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(f" -ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

def start_instances(instance_id):
    try:
        client.start_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} started successfully")
    except Exception as e:
        print(f"Error while starting: {e}")

def stop_instances(instance_id):
    try:
        client.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} successfully stopped")
    except Exception as e:
        print(f"Error while stopping instance: {e}")


