import socketserver

class Counter:
    def __init__(self, name):
        self.value = 0
        self.name = name

    def add(self):
        self.value += 1
        print(f"{self.name}: {self.value}")

    def remove(self):
        self.value -= 1
        print(f"{self.name}: {self.value}")

connected_clients_count = Counter("Connected Clients")


class MyTCPHandler(socketserver.StreamRequestHandler):
    def setup(self):
        super().setup()
        connected_clients_count.add()

    def handle(self):
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

    def finish(self):
        super().setup()
        connected_clients_count.remove()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    host, port = "localhost", 9191
    with ThreadedTCPServer((host, port), MyTCPHandler) as server:
        server.serve_forever()

