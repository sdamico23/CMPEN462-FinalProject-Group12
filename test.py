import random
import math
import sympy
def rsaEncryption():
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
    



    print(d)
    print(e)
    print(n)
    print(n2)
    print(p)
    print(q)
    


        

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

rsaEncryption()