class constructureClass:

    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def start(self):
        print(f"{self.ip}")

    def stop(self):
        print(self.name)


s1 = constructureClass("web1", "192.168.1.10")
s2 = constructureClass("db1", "192.168.1.20")

s1.start()
s1.stop()