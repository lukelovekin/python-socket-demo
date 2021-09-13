from socket import *
serverPort = 11500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is listening")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    if message.decode('utf-8') == 'Hello':
        # ClientSendMessage1 = str(len(str(message))) + " " +  str(message).upper()
        print(message.decode('utf-8'))
        ClientSendMessage1 = "Hello, Whats your name?"
        serverSocket.sendto(ClientSendMessage1.encode(), clientAddress)
    else: 
        print(message.decode('utf-8'))
        ClientSendMessage2 = f'Hello {message.decode("utf-8")}, welcome to SIT202'
        serverSocket.sendto(ClientSendMessage2.encode(), clientAddress)


