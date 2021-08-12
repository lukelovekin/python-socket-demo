from socket import *
serverPort = 11500
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is listening")
while True:
    connectCl1Socket, addr = serverSocket.accept()
    data = connectCl1Socket.recv(1024)
    ClientSendMessage1 = str(len(str(data.decode()))) + " " +  str(data.decode()).upper()
    connectCl1Socket.sendall(ClientSendMessage1.encode())

