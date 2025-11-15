class Server:
    def start(self):
        print("Generic server starting...")


class DatabaseServer(Server):
    def start(self):
        print("Database server starting with DB checks...")

s = Server()
db = DatabaseServer()

s.start()
db.start()