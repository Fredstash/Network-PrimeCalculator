import socket
from sqlite3 import Time
import threading
import os
import pickle
from time import sleep

CORES = os.cpu_count()

HEADERSIZE = 10
THREADS = 6

primes = []

# nickname = input("What is your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.158.110.254", 55558))
# client.connect(("10.158.110.254", 55558))

# https://www.edureka.co/blog/python-program-prime-number/#:~:text=To%20find%20a%20prime%20number,which%20divides%2C%20print%20that%20value.
def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
        return True

def checkAllPrimes(listForPrimes, lock):
    for i in listForPrimes: 
        if isPrime(i):
            lock.acquire()
            print("calling")
            primes.append(i)
            lock.release()
    print("done")



while True:
    full = b""
    new = True
    primes = []
    while True:
        msg = client.recv(16)

        if new:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msgln = int(msg[:HEADERSIZE])
            new = False

        # print(msg)
        # stuff = pickle.loads(msg)
        # print(stuff)
        full += msg

        # print(len(full) - HEADERSIZE)
        # print(msgln)
        if len(full) - HEADERSIZE == msgln:
            # print("full message received")
            # print(full[HEADERSIZE:])

            d = pickle.loads(full[HEADERSIZE:])
            # print(d)

            new = True
            full = b''

            # print(d[1])
            threadList = []
            lock = threading.Lock()
            for thread in range(CORES):
                newList = []
                for stuff in d[1]:
                    if stuff % 6 == thread:
                        newList.append(stuff)
                threadList.append(threading.Thread(target=checkAllPrimes, args=(newList, lock)))
                threadList[thread].start()
            # for x in d[1]:
            #     if isPrime(x):
            #         primes.append(x)

            for x in range(CORES):
                threadList[x].join()

            print(primes)
            dict_primes = {1: primes}
            send_primes = pickle.dumps(dict_primes)
            print(len(send_primes))
            full_send = bytes(f"{len(send_primes):<{HEADERSIZE}}", "utf-8") + send_primes
            client.send(full_send)

            sleep(4)
            client.send("done".encode("ascii"))


    print(full)





# def receive():
#     while True:
#         print("first")
#         try:
#             print('no message yet')
#             message = client.recv(4096)#.decode("ascii")
#             print("found message")
#             if message == "NICK":
#                 client.send(nickname.encode("ascii"))
#             else:
#                 print("HELLO")
#                 printable = pickle.loads(message)
#                 print(f"Here is the info: {printable}")
#         except:
#             print("an error occurred")
#             client.close()
#             break


# def write():
#     while True:
#         message = f"{nickname}: " + input("")
#         client.send(message.encode("ascii"))



# receive_thread =threading.Thread(target=receive)

# receive_thread.start()

# write_thread = threading.Thread(target=write)
# write_thread.start()