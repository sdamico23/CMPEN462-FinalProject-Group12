import socket
###############################################
# Reference --> https://www.journaldev.com/15906/python-socket-programming-server-client
###############################################

#Client program will terminate if user enters “bye” message. 
#Server program will also terminate when client program terminates, this is optional and we can keep 
#server program running indefinitely or terminate with some specific command in client request.

def client_program():
    host = socket.gethostname() # as both code is running on same comp
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()