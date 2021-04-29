import random
import socket


#hostname = socket.gethostname()
#IPaddr = socket.gethostbyname(hostname)
#print("My IP address is: " + IPaddr)

###############################################

# 1) Python socket server program executes at first and wait for any request
# 2) Python socket client program will initiate the conversation at first.
# 3) Then server program will response accordingly to client requests.

#Reference --> https://www.journaldev.com/15906/python-socket-programming-server-client

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # The bind() function takes tuple as argument
    server_socket.bind((host,port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()