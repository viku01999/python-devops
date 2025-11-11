# to store the key value pair


server_config = {"name": "app-server-1", "region": "us-east-1", "status": "running"}

print(server_config["name"])

aws_instance = {"id": "i-0abc12345", "type": "t2.micro", "state": "running"}

print(f"Instance {aws_instance["id"]}")
