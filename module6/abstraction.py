from abc import ABC, abstractmethod


class Server(ABC):
    @abstractmethod
    def start(self):
        pass

class WebServer(Server):
    def start(self):
        print("Web server starting...")

web = WebServer()
web.start()
