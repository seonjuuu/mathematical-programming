#Q2-1
def score(L,k):
    Lcpy = [] #L를 그대로 쓰는건 좋지 않으므로 L를 복사, Lcpy=L로 쓰면 L자체도 바뀜
    for i in L:          #for문 이용하여 L복사
        Lcpy.append(i)
    Lcpy.sort()
    Lcpy=Lcpy[::-1] #역순(내림차순)
    return Lcpy[k-1]

n=[100,93,76,84,88,63,81]
print(score(n,3))

#Q2-2
def list_median(L):
    Lcpy = [] 
    for i in L:          
        Lcpy.append(i)
    Lcpy.sort()    #중앙값은 역순안해도됨
    mid = (len(L)-1)>>1
    return Lcpy[mid]

print(list_median(n))

#Q2-3
def total_time(L):
    ret=0
    for i in range(0,len(L)):
        for j in range(0,i+1):   #자기 자신까지 => i+1
            ret = ret+L[j]
    return ret

#Q2-4
def tis_house(L):
    Lcpy = [] 
    for i in L:          
        Lcpy.append(i)
    Lcpy.sort()    
    mid = (len(L)-1)>>1
    return Lcpy[mid]

H = [5,1,7,9]
print(tis_house(H))

#Q2-5
M2=[[1,1,0,1,1,0],[1,1,0,1,1,0],[1,1,1,1,1,1],[1,1,1,1,0,1]]
# 행 : len(M2)
# 열 : len(M2[0])

def shortest_len(M,i,j):
    q=[]  #큐
    q.append([i,j])  #(i,j):시작점
    v=[]                        # visit
    for n in range(0,len(M)):   #visit 공간 생성
        a=[]
        for k in range(0,len(M[0])):
            a.append(0)
        v.append(a)
    v[i][j]=1
    
    while len(q)!=0:
        row, col = q.pop(0)
        x=[]  #갈 수 있는 위치
        x.append([row,col-1])
        x.append([row,col+1])
        x.append([row-1,col])
        x.append([row+1,col])
        
        for n in x:     #n=[row,col], n[0]=row, n[1]=col
            if 0<=n[0]<len(M) and 0<=n[1]<len(M[0]) and M[n[0]][n[1]]==1 and v[n[0]][n[1]]==0:
                q.append(n)
                v[n[0]][n[1]]=v[row][col]+1 #count 증가
    return v[len(M)-1][len(M[0])-1]   #누적경로가 최단경로

print(shortest_len(M2,0,0))

def shortest_path(M,i,j):
    q=[]  
    q.append([i,j,[[i,j]]])   #경로 정보 추가
    v=[]  
    for n in range(0,len(M)):   
        a=[]
        for k in range(0,len(M[0])):
            a.append(0)
        v.append(a)
    v[i][j]=1
    
    while len(q)!=0:
        row, col, path = q.pop(0) #path:경로
        x=[]  
        x.append([row,col-1])
        x.append([row,col+1])
        x.append([row-1,col])
        x.append([row+1,col])
        
        if row==len(M)-1 and col==len(M[0])-1:  #목적지 도달시 경로 출력
            return path
        
        for n in x:     
            if 0<=n[0]<len(M) and 0<=n[1]<len(M[0]) and M[n[0]][n[1]]==1 and v[n[0]][n[1]]==0:
                new_path = path+[n]     #현재 위치([n]) 추가
                q.append([n[0],n[1],new_path])  #
                v[n[0]][n[1]]=v[row][col]+1 
    return []
print(shortest_path(M2,0,0))
            
    
#Q3-1
def map_index(L):
    Lcpy = []
    for i in L:
        Lcpy.append(i)
    Lcpy.sort()
    ret = []
    for i in Lcpy:
        ret.append(L.index(i))
    return ret

L=[1,4,2,6,7]
print(map_index(L))

#Q3-2
def print_kthlarge(L,k):
    Lcpy=[]
    for i in L:
        Lcpy.append(i)
    Lcpy.sort()
    Lcpy=Lcpy[::-1]
    return Lcpy[k-1]

L=[2,1,6,4,7]
print(print_kthlarge(L,2))

#Q3-3
def num_coin(L,k):
    cnt=0
    Lcpy = L[::-1]
    tmp = k
    for i in Lcpy:
        cnt = cnt+(tmp//i)
        tmp = tmp%i
    return cnt

L=[1,5,10,50,100,500,1000,5000,10000,50000]
print(num_coin(L,4790))

#Q3-4
def dfs(n,m,M,color):
    if n<=-1 or n>=len(M) or m<=-1 or m>=len(M[0]):
        return False
    if M[n][m]==color:
        M[n][m]=5  #visit를 만들지 않고, 그냥 방문했다면 5라고 설정(다른수들도 상관없음, color인 0,1,2만 빼고)
        dfs(n-1,m,M,color)
        dfs(n+1,m,M,color)
        dfs(n,m-1,M,color)
        dfs(n,m+1,M,color)
        return True
    return False


def num_area(M):
    L=[0,0,0] #L[0]=0으로 칠해진 구역 수, L[1]=1로 칠해진 구역수 ... -> 결과=L[0]+L[1]+L[2]
    for i in range(0,3):  # i는 색을 나타냄
        for n in range(0,len(M)):  #row
            for m in range(0,len(M[0])):  #col
                if dfs(n,m,M,i)==True:
                    L[i]=L[i]+1
                    
    return sum(L)

M=[[0,0,0,1,1],[2,2,1,1,1],[2,2,2,1,1],[2,2,1,1,1],[0,0,0,0,0]]
print(num_area(M))