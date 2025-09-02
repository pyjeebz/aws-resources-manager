import argparse
from s3_manager import list_buckets, create_bucket
from ec2_manager import list_instance, start_instance, stop_instance
from export_manager import export_to_json, export_to_csv

def entryPointForCli():
    parser = argparse.ArgumentParser(description="AWS Resources Manager CLI")

    subparsers = parser.add_subparsers(dest="service")

    #s3 Commands
    s3_parser = subparsers.add_parser("s3", help="Manage S3 Buckets")
    s3_parser.add_argument("action", choices=["list", "create"], help="Action to perform")
    s3_parser.add_argument("--name", help="Bucket name (reqired for creating bucket)")

    #EC2 Commands

    ec2_parser = subparsers.add_parser("ec2", help="Manage EC2 Instances")
    ec2_parser.add_argument("action", choices=["list", "start", "stop"], help="Action to perform")
    ec2_parser.add_argument("--id", help="Instance ID (required for creating instances, start/stop)")

    #Export Commands
    export_parser = subparsers.add_parser("export", help="This is to export data")
    export_parser.add_argument("action", choices=["export_to_json","export_to_csv"], help="Action to perform")
    export_parser.add_argument("--data", help="Export to data to either json or csv file")

    args = parser.parse_args()

    if args.service == "s3":
        if args.action == "list":
            list_buckets()
        elif args.action == "create":
            if not args.name:
                print("Error: --name is required to create bucket")
            else:
                create_bucket(args.name)

    elif args.service =="ec2":
        if args.action == "list":
            list_instance()
        elif args.action == "start":
            if not args.id:
                print("Error: --id is needed to start an instance")
            else:
                start_instance(args.id)
        elif args.action == "stop":
            if not args.id:
                print("Error: --id is needed to stop an instance")
            else:
                stop_instance(args.id)
        
        elif args.service == "export":
            if args.format == "json":
                export_to_json(args.data or "{}", "output.json")
            elif args.format == "csv":
                export_to_csv([args.data or "sample,data"], "output.csv")
    
    if entry == "entryPointForCli":
        entryPointForCli()
