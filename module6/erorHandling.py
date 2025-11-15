import time

class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def start(self):
        try:
            print(f"Starting server {self.name}...")
            if self.name == "web1":
                raise Exception("Server failed to start.")
            print(f"Server {self.name} started.")
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)
            self.start()


server1 = Server("web1", "192.168.1.10")
server1.start()
