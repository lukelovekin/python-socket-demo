from socket import *
serverName = '127.0.0.1'
serverPort = 11500
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Hello message send
message = "Hello"
clientSocket.sendto(message.encode(), (serverName, serverPort))
ServerReply, serverAddress = clientSocket.recvfrom(2048)

print(ServerReply.decode())

# Name response
message  = input()
clientSocket.sendto(message.encode(), (serverName, serverPort))
ServerReply, serverAddress = clientSocket.recvfrom(2048)

print(ServerReply.decode())


clientSocket.close()
