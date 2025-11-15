import logging

class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

    def start(self):
        self.logger.info(f"Starting server {self.name} at {self.ip}")

    def stop(self):
        self.logger.warning(f"Stopping server {self.name}")


server1 = Server("web1", "192.168.1.10")
server1.start()
server1.stop()
