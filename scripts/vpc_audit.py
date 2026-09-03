import boto3

session = boto3.Session(
    profile_name="cloud-lab",
    region_name="us-east-1"
)

ec2 = session.client("ec2")

vpcs = ec2.describe_vpcs()["Vpcs"]

print("\n=== AWS VPC SECURITY AUDIT ===\n")

for vpc in vpcs:
    vpc_id = vpc["VpcId"]
    cidr = vpc["CidrBlock"]
    is_default = vpc["IsDefault"]

    print(f"VPC ID: {vpc_id}")
    print(f"CIDR: {cidr}")
    print(f"Default VPC: {is_default}")

    route_tables = ec2.describe_route_tables(
        Filters=[
            {
                "Name": "vpc-id",
                "Values": [vpc_id]
            }
        ]
    )["RouteTables"]

    internet_routes = []

    for route_table in route_tables:
        for route in route_table["Routes"]:
            if route.get("DestinationCidrBlock") == "0.0.0.0/0":
                internet_routes.append(route)

    if internet_routes:
        print("Internet route detected: YES")
    else:
        print("Internet route detected: NO")

    print("-" * 40)

print("\n=== SECURITY GROUP SSH AUDIT ===\n")

security_groups = ec2.describe_security_groups()["SecurityGroups"]

for sg in security_groups:
    sg_name = sg["GroupName"]
    sg_id = sg["GroupId"]

    ssh_open_to_world = False

    for permission in sg["IpPermissions"]:
        from_port = permission.get("FromPort")
        to_port = permission.get("ToPort")

        if from_port == 22 and to_port == 22:
            for ip_range in permission.get("IpRanges", []):
                if ip_range.get("CidrIp") == "0.0.0.0/0":
                    ssh_open_to_world = True

    print(f"Security Group: {sg_name} ({sg_id})")

    if ssh_open_to_world:
        print("WARNING: SSH port 22 is open to 0.0.0.0/0")
    else:
        print("OK: SSH is not open to 0.0.0.0/0")

    print("-" * 40)
