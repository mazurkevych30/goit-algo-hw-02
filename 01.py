from queue import Queue
import random

class Request:
    def __init__(self, name):
        self.name = name

class Server:
    def __init__(self):
        self.requests = Queue()

    def generate_request(self):
        req_id = {random.randint(1,100)}
        self.requests.put(Request(f"request - {req_id}"))
        print(f"New request - {req_id} added to the queue.")

    def process_request(self):
        if not self.requests.empty():
            current_request = self.requests.get()
            print(f"The {current_request.name} processed.")
        else:
            print("The queue is empty.")

def commands_list():
    print("Commands:")
    print("g - for generate request")
    print("p - for process request")
    print("h - to view the list of commands")
    print("q - close script")

def main():
    server = Server()
    commands_list()
    while True:
        user_input = input("Input command: ").strip().lower()

        match user_input:
            case "g":
                server.generate_request()
            case "p":
                server.process_request()
            case "h":
                commands_list()
            case "q":
                print("Closed.")
                break
            case _:
                print("Invalid command.")



if __name__ == "__main__":
    main()
