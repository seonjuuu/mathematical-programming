def karatsuba(a,b):
    ah = a>>512
    al = a&(2**512-1)
    bh = b>>512
    bl = b&(2**512-1)
    ch = ah*bh
    cl = al*bl
    cm = (ah+al)*(bh+bl)-ch-cl
    ret = ch<<1024
    ret = ret + cl
    ret = ret + (cm<<512)
    return ret

def schoolbook_poly(a,b):
    c=[]
    for i in range(0, len(a)+len(b)):
        c.append(0)
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            c[i+j]=c[i+j]+a[i]*b[j]  #c[0]:상수곱 c[1]:1차식 c[2]:2차식
    return c

f=[1,1]
g=[2,3]

h = schoolbook_poly(f,g)
print(h)

#f,g랑 차수가 같음
def karatsuba_poly(f,g):
    hlen = len(f)>>1
    fl=[]
    fh=[]
    gl=[]
    gh=[]
    for i in range(0,hlen):
        fl.append(f[i])
    for i in range(0,hlen):
        fh.append(f[i+hlen])
    for i in range(0,hlen):
        gl.append(g[i])
    for i in range(0,hlen):
        gh.append(g[i+hlen])
    # flgl, fhgh
    flgl = schoolbook_poly(fl,gl)
    fhgh = schoolbook_poly(fh,gh)
    
    for i in range(0,hlen):
        fh[i]=fh[i]+fl[i]   # fh+fl
    for i in range(0,hlen):
        g[i]=gh[i]+gl[i]    # gh+gl
        
    cm = schoolbook_poly(fh,gh)
    # cm = (fh+fl)(gh+gl)-flgl-fhgh
    for i in range(0,hlen):
        cm[i] = cm[i]-flgl[i]-fhgh[i]
    
    #합치기(자릿수 고려)
    c=[]
    for i in range(0,len(f)+len(g)):
        c.append(0)
    for i in range(0,len(f)):
        c[i]=flgl[i]
        c[i+len(f)]=fhgh[i]
    for i in range(0,len(f)):
        c[i+hlen]=c[i+hlen]+cm[i]        
    
    return c

import random
f=[]
g=[]

for i in range(0,10):
    f.append(random.randrange(0,10))
    g.append(random.randrange(0,10))
h = karatsuba_poly(f,g)
k = schoolbook_poly(f,g)

print(h)
print(k)

##행렬곱##
def martix_mul(A,B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])
    if colA != rowB:
        return 0
    C=[]  # 빈공간 행렬
    for i in range(0,rowA):
        a=[] # 각 행을 만들 빈 공간
        for j in range(0,colB):
            a.append(0) # 각 행마다 열을 0씩 채워줌
        C.append(a) # [[0,0],[0,0]]
    for i in range(0,rowA): # AxB에서 A의 한 행씩 진행
        for j in range(0,colB): #B의 열씩 진행
            for k in range(0,colA): #원소끼리 내적
                C[i][j]=C[i][j]+A[i][k]*B[k][j]
                
    return C

A=[[1,2,3],[4,5,6]]
B=[[3,2],[1,2],[1,0]]
print(martix_mul(A,B))


##Strassen
def split_mat(A):
    row = len(A)
    hrow = row >> 1
    a=[]
    for i in range(0,hrow):
        tmp=[]
        for j in range(0,hrow):
            tmp.append(A[i][j])
        a.append(tmp)
    b=[]
    for i in range(0,hrow):
        tmp=[]
        for j in range(0,hrow):
            tmp.append(A[i][j+hrow])
        b.append(tmp)
    c=[]
    for i in range(0,hrow):
        tmp=[]
        for j in range(0,hrow):
            tmp.append(A[i+hrow][j])
        c.append(tmp)
    d=[]
    for i in range(0,hrow):
        tmp=[]
        for j in range(0,hrow):
            tmp.append(A[i+hrow][j+hrow])
        d.append(tmp)   
    
    return a,b,c,d

def mat_add(A,B):
    row = len(A)
    col = len(A[0])
    C=[]
    for i in range(0,row):
        a=[]
        for j in range(0,col):
            a.append(0)
        C.append(a)
    for i in range(0,row):
        for j in range(0,col):
            C[i][j] = A[i][j]+B[i][j]
    return C

def mat_sub(A,B):
    row = len(A)
    col = len(A[0])
    C=[]
    for i in range(0,row):
        a=[]
        for j in range(0,col):
            a.append(0)
        C.append(a)
    for i in range(0,row):
        for j in range(0,col):
            C[i][j] = A[i][j]-B[i][j]
    return C

#항상 nxn
def matmul_stra(A,B):
    row = len(A)
    hrow = row >> 1
    #행렬 쪼개기
    a,b,c,d = split_mat(A)
    e,f,g,h = split_mat(B)
    # p1 = a(f-h)
    fh = mat_sub(f,h)
    p1 = martix_mul(a,fh)
    ab = mat_add(a,b)
    p2 = martix_mul(ab,h)
    cd = mat_add(c,d)
    p3 = martix_mul(cd,e)
    ge = mat_sub(g,e)
    p4 = martix_mul(d,ge)
    ad = mat_add(a,d)
    eh = mat_add(e,h)
    p5 = martix_mul(ad,eh)
    bd = mat_sub(b,d)
    gh = mat_add(g,h)
    p6 = martix_mul(bd,gh)
    ac = mat_sub(a,c)
    ef = mat_sub(e,f)
    p7 = martix_mul(ac,ef)
    
    C=[]
    for i in range(0,row):
        a=[]
        for j in range(0,row):
            a.append(0)
        C.append(a)
    # C = nxn
    for i in range(0,hrow):
        for j in range(0,hrow):
            C[i][j] = p5[i][j]+p4[i][j]-p2[i][j]+p6[i][j]
    for i in range(0,hrow):
        for j in range(0,hrow):
            C[i][j+hrow] = p1[i][j]+p2[i][j]
    for i in range(0,hrow):
        for j in range(0,hrow):
            C[i+hrow][j] = p3[i][j]+p4[i][j]
    for i in range(0,hrow):
        for j in range(0,hrow):
            C[i+hrow][j+hrow] = p1[i][j]+p5[i][j]-p3[i][j]-p7[i][j]
    
    return C
            
            
A=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
B=[[1,0,1,1],[1,0,1,1],[1,0,1,1],[1,0,1,1]]
print(matmul_stra(A,B))
print(matmul_stra(A,B))

