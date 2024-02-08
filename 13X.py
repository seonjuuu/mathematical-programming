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
        y = mod_exp(a,r,n)                #  2.2
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
        
def ext_gcd(a,b):
    x=a
    y=b
    g=1
    while x&1==0 and y&1==0:
        x = x>>1
        y = y>>1
        g = g<<1
    u=x
    v=y
    A=1
    B=0
    C=0
    D=1
    flag = 0
    while flag==0:
        while u&1==0 :
            u = u>>1
            if A&1==0 and B&1==0:
                A=A>>1
                B=B>>1
            else:
                A=(A+y)>>1
                B=(B-x)>>1
        while v&1==0:
            v=v>>1
            if C&1==0 and D&1==0:
                C = C>>1
                D = D>>1
            else:
                C = (C+y)>>1
                D = (D-x)>>1
        if u>=v:
            u = u-v
            A = A-C
            B = B-D
        else:
            v=v-u
            C=C-A
            D=D-B
        if u==0:
            flag=1
            return C,D,g*v
        else:
            flag==0

# gcd(a,n)=1 => a*[]=1modn

def mod_inv(a,n): #a^-1 mod n
    x,y,d = ext_gcd(a,n)
    if d==1:
        return x
    else:
        return 0


# (g**e)%n      
def mod_exp(g,e,n):
    A=1
    nbit = e.bit_length() #3
    k = 1<<(nbit-1)       #bit를 읽음 1<<2 = 0x100
    cnt = nbit-1          #이동시킴
    for i in range(0, nbit):
        A=(A*A)%n 
        chk = (e&k)>>cnt  #e%K:1인지0인지 읽어주고 cnt이용해서 그 자릿수 비트만 가져옴
        if chk == 1 :
            A=(A*g)%n
        cnt=cnt-1
        k=k>>1
    return A

g=2
e=5
n=10
print("my exp:",mod_exp(2,5,10))
    
#slvl=1024 -> RSA-1024
#소수 = 512 -> 2**512  
def rsa_keygne(slvl):
    flag=0
    e = 2**16+1
    while flag==0:
        pf=0
        while pf==0:
            p = random.randrange(1,2**(slvl>>1))
            p = p|1 #강제로 홀수로 만듦
            pf = MillerRabin(p,4)
        pf=0
        while pf==0:
            q=random.randrange(1,2**(slvl>>1))
            q=q|1
            pf = MillerRabin(q,4)
        n=p*q
        phin = (p-1)*(q-1)
        x,y,g = ext_gcd(e,phin)
        if g==1:
            flag=1
            if x<=0:
                d = x+phin
            else:
                d=x
                
    dp = d%(p-1)
    dq = d%(q-1)
    qinv = mod_inv(q,p)
    return e,d,dp,dq,qinv,n,p,q,phin

e,d,dp,dq,qinv,n,p,q,phin = rsa_keygne(512)
print("public key:",e)
print("modulus:",n)
print("private key:",d)
print("private key dp:",dp)
print("private key dq:",dq)
print("private key qinv:",qinv)
print("chk:", (e*d)%phin)

def rsa_enc(m,e,n):
    #(m**e)%n
    c=mod_exp(m,e,n)
    return c

def rsa_dec(c,d,n):
    #(c**d)%n
    m = mod_exp(c,d,n)
    return m


#14주차
def rsa_dec_crt(c,dp, dq, qinv,p,q,n):
    m1 = mod_exp(c,dp,p)
    m2 = mod_exp(c,dq,q)
    h = (qinv)*(m1-m2)
    h = h%p
    m = m2+h*q
    m = m%n
    return m
    
    

m = random.randrange(1,100000)
print("original message:",m)
c=rsa_enc(m,e,n)
print("ciphertext:",c)
pori=rsa_dec(c,d,n)
print("plaintext:",pori)
pcrt = rsa_dec_crt(c,dp,dq,qinv,p,q,n)
print("plaintext crt:",pcrt)

#Review

def num_com1(a,b):
    ret = mod_exp(a,b,10)
    if ret==0:
        ret=10
    return ret

def num_com2(a,b):
    #2로 나눈 나머지
    x1 = a&1
    #5로 나눈 나머지
    a5 = a%5
    r = b&3 #(a5**r)%5
    x2 = (a5**r)%5
    ret = (5*x1+6*x2)%10
    return ret

print(num_com1(7,100))
print(num_com1(9,635))
print(num_com2(7,100))
print(num_com2(9,635))
