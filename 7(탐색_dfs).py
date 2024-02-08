##review1##
##경우1
def naive_cnt(L,n):
    cnt = 0
    for i in range(0,len(L)):
        if L[i] == n:
            cnt = cnt+1
    return cnt

L = [6,3,2,10,10,10,-10,-10,7,3]
F = [10,9,-5,2,3,4,5,-10]

k=[]
for i in range(0,len(F)):
    cnt = naive_cnt(L,F[i])
    k.append(cnt)
print(k)
    
##경우2 (binary search 이용)
def merge(left,right,L):
    lleft = len(left)
    lright = len(right)
    i=0 # L
    l=0 # left
    r=0 # right
    while l<lleft and r<lright:
        if left[l]<right[r]:
            L[i]=left[l]
            l=l+1
            i=i+1
        else:
            L[i]=right[r]
            r=r+1
            i=i+1
    while l<lleft:
        L[i]=left[l]
        l=l+1
        i=i+1
    while r<lright:
        L[i]=right[r]
        r=r+1
        i=i+1

def msort(L):
    if len(L)<=1:
        return L
    middle = len(L)>>1
    left = L[:middle]
    right = L[middle:]
    msort(left)
    msort(right)
    merge(left,right,L)
    return L

L=[6,3,2,10,10,10,-10,-10,7,3]
F=[10,9,-5,2,3,4,5,-10]

#binary 하기 전에 먼저 정렬(sort)
msort(L)
print(L)

def bsearch(L,n):
    start=0
    end = len(L)-1
    while start<=end:
        middle = (start+end)>>1
        if L[middle]<n: #[   | (n) ]
            start =middle+1
        elif L[middle]>n: #[ (n) |  ]
            end =middle-1
        else:
            return middle
    return -1

def bsearch_h(L,n):
    start =0
    end = len(L)-1
    high=-1
    while start<=end:
        middle = (start+end)>>1
        if L[middle]<n: #[|(n)]
            start = middle+1
        elif L[middle]>n: #[ n | ]
            end = middle-1
        else:  
            high = middle # [  33  ]
            start = middle+1
    return high

def bsearch_l(L,n):
    start =0
    end = len(L)-1
    low=-1
    while start<=end:
        middle = (start+end)>>1
        if L[middle]<n: #[|(n)]
            start = middle+1
        elif L[middle]>n: #[ n | ]
            end = middle-1
        else:  
            low = middle # [  33  ]
            end = middle-1
    return low

high = bsearch_h(L,10) #10의 원소가 있는 인덱스의 상한 인덱스
low = bsearch_l(L,10) #10의 원소가 있는 인덱스의 하한 인덱스
print("upper bound :", high) 
print("lower bound :", low) 

#bsearch-경우1
def cnt_final(L,n):
    high = bsearch_h(L,n)
    if high==-1:
        return 0
    low = bsearch_l(L,n)
    return high-low+1

print("find final:",cnt_final(L,-10))

#bsearch-경우2
def cnt_second(L,n):
    idx = bsearch(L,n)
    print(idx)
    if idx==-1:
        return 0
    cnt=0
    for i in range(idx, len(L)): #idx부터 오른쪽
        if L[i]==n:
            cnt=cnt+1
    for i in range(0, idx):  #idx부터 왼쪽
        if L[i]==n:
            cnt=cnt+1
    return cnt

print(cnt_second(L,3))


##review2##
n=7
m=6
L=[]
for i in range(0,n+1): #0번째 자리는 빈공간으로 만들기-> n+1 
    L.append([])
print(L)

for i in range(0,m):
    tmp = list(map(int,input().split()))
    # tmp[0] = 1 tmp[1] = 2 => (1-2)
    # tmp[0] = 1 tmp[1] = 5 => (1-5)
    #[][2,5][1][][][1][]
    L[tmp[0]].append(tmp[1]) #1번 리스트에 2를 추가
    L[tmp[1]].append(tmp[0]) #2번 리스트에 1를 추가

def dfs(L,v,visited):
    visited.append(v)
    for i in L[v]:
        if i not in visited:
            dfs(L,i,visited)
            
def cnt_worm(L,n):
    visited = []
    dfs(L,n,visited)
    print(visited)
    cnt = len(visited)
    return cnt-1       #자기자신 빼주기
    
print(L)
print(cnt_worm(L,1))
    