from random import randint
import threading
import socket
import pickle


class client(threading.Thread):
    def __init__(self, client_num, total_nums):
        super().__init__()
        self.client_num = client_num
        self.total_nums = total_nums

    def run():
        pass

host = "10.158.110.254"
port = 55558
# port = 55558

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

clients = []
nicknames = []
# nums = []
HEADERSIZE = 10
# stuff = []
shift = 0

def receive(lock):
    while True:
        stuff = []
        client, address = server.accept()
        print(f"connected with {str(address)}" )

        global shift

        # for i in range(10):
        #     nums.append(i)
        lock.acquire()
        shiftb = shift
        shift+= 100000
        for i in range(shiftb, shift):
            stuff.append(i)
        print(shift)
        print(shiftb)
        lock.release()

        print("made it")
        nums = {1: stuff}

        data_send = pickle.dumps(nums)

        full = bytes(f"{len(data_send):<{HEADERSIZE}}", "utf-8") + data_send
        client.send(full)

        t1 = threading.Thread(target=getInfo, args=(client, address))
        t1.start()

        




# gets new clients and starts threads
def listen():
    pass


# breaks up the work based on clients and sends them to work
def boss():
    pass

def getInfo(client, address):
    new_msg = True
    full_msg = b''
    while True:
        data_receive = client.recv(16)

        if data_receive == "done".encode("ascii"):
            break


        if new_msg:
            print("called")
            msgln = int(data_receive[:HEADERSIZE])
            new_msg = False

        full_msg += data_receive

        if len(full_msg) - HEADERSIZE == msgln:
            # print("full message received")
            # print(full[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            # print(d)

            new_msg = True
            full_msg = b''

            for x in d[1]:
                print(f'{x} is prime')
    print("all done")

    # t3 = threading.Thread(target=receive, args=())
    # t3.start()

        


# def broadcast(message):
#     for client in clients:
#         client.send(message)

# def handle(client, nums):
#     data_string = pickle.dumps(nums)
#     print(data_string)
#     client.send(data_string)
#     while True:
#         try:
#             message = client.recv(1024)
#             # broadcast(message)
#             print(message)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadcast(f'{nickname} left the chat'.encode('ascii'))
#             nicknames.remove(nickname)
#             break

# def numbers_to_send(start):
#     nums = []
#     for i in range(start, 100000000, len(clients)):
#         nums.append(i)


# def receive():
#     while True:
#         client, address = server.accept()
#         print(f"connected with {str(address)}" )

#         nums = []
#         for i in range(100):
#             nums.append(i)

#         # client.send('NICK'.encode("ascii"))
#         nickname = client.recv(1024).decode("ascii")
#         nicknames.append(nickname)
#         clients.append(client)
#         broadcast(f"{nickname} joined the chat".encode("ascii"))
#         # client.send("connected to the server".encode("ascii"))
#         nums = []
#         thread = threading.Thread(target=handle, args=(client, nums))
#         thread.start()

# print("server is listening...")
# receive()


# import threading
# import socket

# host = "10.15.57.255"
# port = 55556

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((host, port))
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message):
#     for client in clients:
#         client.send(message)

# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             # broadcast(message)
#             print(message)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadcast(f'{nickname} left the chat'.encode('ascii'))
#             nicknames.remove(nickname)
#             break

# def receive():
#     while True:
#         client, address = server.accept()
#         print(f"connected with {str(address)}" )

#         client.send('NICK'.encode("ascii"))
#         nickname = client.recv(1024).decode("ascii")
#         nicknames.append(nickname)
#         clients.append(client)
#         broadcast(f"{nickname} joined the chat".encode("ascii"))
#         client.send("connected to the server".encode("ascii"))

#         thread = threading.Thread(target=handle, args=(client,))
#         thread.start()

lock = threading.Lock()
t2 = threading.Thread(target=receive, args=(lock,))
t2.start()
print("server is listening...")