from socket import *
serverName = '127.0.0.1'
serverPort = 11500
clientSocket = socket(AF_INET, SOCK_STREAM)
message = "Hello Joe"
clientSocket.connect((serverName, serverPort))
clientSocket.sendto(message.encode(), (serverName, serverPort))
ServerReply = clientSocket.recv(1024)
print(ServerReply.decode())
clientSocket.close()
