# Overview

I really wanted to learn how networking worked, I feel like it is very important to understand how different devices can connect to eachother.

I created a distributed network capable of easily calculating potential prime numbers. You have to start the server and client in on separate devices (on the same network) or in two terminals on one device, once the server is started you can add clients which will immediately be sent work and begin calculating potential primes

{Describe your purpose for writing this software.}
My purpose in designing this is to understand networking at a deeper level, and eventually learn how to incorporate sockets into the OS I am developing (so the OS can use networking to increase speed).


[Software Demo Video](https://youtu.be/UFNLoYdOKRg)

# Network Communication

I uses a client to server architecture. THe purpose is that a server computer will be able to distribute its work to several different devices

I'm using TCP so that there is verifcation on the packets, and I'm using port 55558, which is just to avoid the computer ports

The data I am sending is being pickled and has a header tacked on telling the client how much data it is receiving 

# Development Environment

I used Visual Studio Code
I coded it in python


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Youtube socket tutorial](https://www.google.com/search?q=pickle+in+networking+python&oq=pickle+in+networking+python&aqs=chrome..69i57j0i22i30j0i390l4.5677j1j7&sourceid=chrome&ie=UTF-8#kpvalbx=_xErKYvSdE8TG0PEPicqE4A417)
* [Youtube chat room (The last block of the tutorial specifically)](https://www.youtube.com/watch?v=FGdiSJakIS4)

# Future Work

* Send more work to each client.
* Understand sockets on a lower level.
* Send instructions before the header so the client can do more than one thing.