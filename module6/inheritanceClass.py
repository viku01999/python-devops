class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def start(self):
        print(f"{self.name} started at {self.ip}")


class WebServer(Server):
    def deploy_code(self):
        print(f"Deploying code to {self.name}")


web = WebServer("web1", "192.168.1.10")

web.start() 

web.deploy_code() 