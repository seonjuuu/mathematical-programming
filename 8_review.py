'''
#review1
#BFS 이용
n=7
m=6
L=[]
for i in range(0,n+1):
    L.append([])

for i in range(0,m):
    tmp = list(map(int,input().split()))
    L[tmp[0]].append(tmp[1])
    L[tmp[1]].append(tmp[0])

def cnt_com(L,v):
    q=[]
    visited=[]
    q.append(v)
    visited.append(v)
    while len(q)!=0:
        n=q.pop(0)
        for i in L[n]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    
    return len(visited)-1

print(cnt_com(L,1))
'''
#review2
M=[[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
# row = len(M)
# col = len(M[0])

# 입력 : 행렬 M, 시작점 [i,j]
def shortest_len(M,i,j):
    q=[]
    q.append([i,j])
    v=[]
    for n in range(i,len(M)): # 한 행씩
        a=[]
        for k in range(0,len(M[0])): # 한 열씩
            a.append(0)
        v.append(a)
    v[i][j]=1
    
    while len(q)!=0:
        row, col = q.pop(0) # [i,j]
        x=[]
        x.append([row,col-1])
        x.append([row,col+1])
        x.append([row-1,col])
        x.append([row+1,col])
        
        for n in x : 
            if 0<=n[0]<len(M) and 0<=n[1]<len(M[0]) and M[n[0]][n[1]] == 1 and v[n[0]][n[1]]==0:
                q.append([n[0],n[1]])
                v[n[0]][n[1]]=v[row][col]+1  #이전의 값의 1을 더함
                
    return v[len(M)-1][len(M[0])-1]

print(shortest_len(M,0,0))

##review3
A=[3,5,1,2]
B=[7,0,3]
def merge_and_sort(A,B):
    C=A+B
    msort(C)
    return C

def sort_and_merge(A,B):
    msort(A)
    msort(B)
    # mergesort에서 merge 구현한다
    ret = []
    a=0
    b=0
    alen = len(A)
    blen = len(B)
    while a<alen and b<blen:
        if A[a]<B[b]:
            ret.append(A[a])
            a=a+1
        else:
            ret.append(B[b])
            b=b+1
    while a<alen:
        ret.append(A[a])
        a=a+1
    while b<blen:
        ret.append(B[b])
        b=b+1
    return ret

print(sort_and_merge(A,B))

#review4
L=[2,4,1,6,3,7,9]

def total_time(L):
    msort(L)
    ret=0
    for i in range(0,len(L)):
        for j in range(0,i+1):
            ret = ret+L[j]
    return ret

print(total_time(L))