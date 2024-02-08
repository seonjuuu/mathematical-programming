import random

def MillerRabin(n,t):
    # n-1 = 2^s*r
    tmp = n-1
    s=0
    while (tmp%2==0):     # 1
        tmp = tmp>>1
        s = s+1
    r=n-1 #n-1/2**s
    for i in range(0,s):
        r=r>>1              
    for i in range(0,t):
        a = random.randrange(2,10)  #  2.1
        y = (a**r)%n                #  2.2
        if y != 1 and y != n-1 :    #  2.3
            j=1
            while j<=s-1 and y != n-1:
                y=(y*y)%n
                if y==1:
                    return 0
                j = j+1
            if y != n-1:
                return 0
    return 1
        
print(MillerRabin(41,1)) #4*10=2^3(s)*5(r)