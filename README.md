# AWS Resources Manager

A simple CLI to automate and manage AWS resources and exports results to JSON and CSV files.

## Features
- Create bucket
- List bucket
- Create/Start/Stop EC2 instances
- Export results to either JSON or CSV files

## How it works

```bash
# List S3 buckets
python aws_manager.py s3 list

#Start EC2 Instance
python aws_manager.py start --id <instanceId>

# Export EC2 instances to JSON

python aws_manager.py ec2 list --format json --output instances.json