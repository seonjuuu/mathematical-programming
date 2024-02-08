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
    
def rsa_keygne():
    flag=0
    while flag==0:
        p = random.randrange(1,1000)
        p = p|1 #강제로 홀수로 만듦
        flag = MillerRabin(p,4)
    flag=0
    while flag==0:
        q=random.randrange(1,1000)
        q=q|1
        flag = MillerRabin(q,4)
    print("p,q",p,q)
    n=p*q
    phin = (p-1)*(q-1)
    flag=0
    while flag==0:
        e = random.randrange(1,phin)
        x,y,g = ext_gcd(e,phin)
        if g==1:
            flag=1
            if x<=0:
                d = x+phin
            else:
                d=x
    return e,d,n,phin

e,d,n,phin = rsa_keygne()
print("public key:",e)
print("modulus:",n)
print("private key:",d)
("chk:", (e*d)%phin)

A=[[1,2,3],[4,5,6],[7,8,9]]
A=[1,2,3,4,5,6,7,8,9]
L=[0]*9
for i in range(0,3): #i는 행
    for j in range(0,3): #j는 열
        L[i*3+j]=1
        
N=3
B=[0]*(N*N) #길이 NxN인 행렬 생성
for i in range(0,N):
    for j in range(0,N):
        B[i*N+j]=(i+1)*(j+1)
        
print(B)
B.sort()
k=7
print(B[k])

#B=[1,2,2,3,3,4,6,6,9]
# [1,.....,m,.....,k]
N=3
k=7
start=1
end=k
res = 0
while start<=end:
    m=(start+end)>>1
    cnt=0
    for i in range(1,N+1):
        cnt=cnt+min(m//i,N)
    if cnt>=k:
        res = m
        end = m-1
    else:
        start = m+1


        
    
    