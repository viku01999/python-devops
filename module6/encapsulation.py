class Server:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


s = Server("web1")
print(s.get_name())
s.set_name("web2")
print(s.get_name())