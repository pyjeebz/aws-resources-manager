import boto3

client = boto3.client('ec2')

def list_instance():
    response = ec2.describe_instance()
    print("EC2 instance(s) created:")
    for reservation in response ["Reservations:"]:
            for instance in reservation ["Instances"]:
                  print(f" -ID:{instance['instanceId']}, State: {instance['State'],['Name']}")

def start_instance(instance_id):
      try:
            ec2.start_instance(InstanceIds=(instance_id))
            print(f"Instance {instance_id} started successfully")
      except Exception as e:
            print(f"Error while starting: {e}")

def stop_instance(instance_id):
      try:
            ec2.stop_instance(InstanceIds=(instance_id))
            print(f"Instance {instance_id} successfully stopped")
      except Exception as e:
            print (f"Error while stopping instance: {e}")
            

