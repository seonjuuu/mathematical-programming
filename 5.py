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

#순차탐색
def linear_search(L,n):
    for i in range(0,len(L)):
        if L[i]==n:
            return i
    return -1

L = [9,8,1,2,7,3,6,4,5]
#print(linear_search(L,3))

#이진탐색
def Binary_search(L,n):
    start = 0
    end = len(L)-1
    
    while(start <= end):
        middle = (start+end)>>1
        if L[middle] < n :
            start = middle+1
        elif L[middle] > n :
            end = middle-1
        else :
            return middle
    return -1

#시작
###1
n = 5
A = [8,3,7,9,2]
m = 3
B = [5,7,9]

#binary search  이용하기 위해서 -> sort 
msort(A)
print(A)

for i in range(0,m):
    chk = Binary_search(A,B[i])
    if chk ==-1:
        print("no", end=' ')
    else:
        print("yes", end=' ')
        

###2 #중복제거
B=[1,4,2,3,1,4,2,3,1,2]

#경우1
def delete_and_sort(B):
    C=[]
    for i in range(0, len(B)):
        chk = linear_search(C,B[i])
        if chk == -1:           #중복되지 않은것들만 추가
            C.append(B[i])
    msort(C)
    return C

#경우2
def sort_and_delete(B):
    Btmp=B
    msort(Btmp)
    D=[]
    for i in range(0, len(Btmp)):
        chk = Binary_search(D,Btmp[i])
        if chk == -1:
            D.append(Btmp[i])
    return D

#시간 비교
import time

first=0
second=0

for i in range(0, 1):
    start = time.time()
    delete_and_sort(B)
    end = time.time()
    first = first+(end-start)
    start = time.time()
    sort_and_delete(B)
    end = time.time()
    second = second+(end-start)

print(f"first : {first:.5f} sec")
print(f"second : {second:.5f} sec")  


###3
#빈도수 정렬하기
C = [11,33,11,77,54,11,25,25,33]

def lsearch_list(L,n):
    for i in range(0,len(L)):
        if L[i][0] == n:
            return i
    return -1

L=[]
 
for i in range(0,len(C)):
    chk = lsearch_list(L,C[i])
    if chk == -1:
        L.append([C[i],1])
    else:
        L[chk][1]=L[chk][1]+1
        
#L=[[숫자[0], 등장횟수[1]]
print(L)

def merge_list(left,right,L):
    lleft = len(left)
    lright = len(right)
    i=0 # L
    l=0 # left
    r=0 # right
    while l<lleft and r<lright:
        if left[l][1]>=right[r][1]:  #빈도수(리스트[1])로 비교 => (빈도수가 많은것은 먼저 나오도록) + (먼저나온것이 먼저 나오도록)
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

def msort_list(L):
    if len(L)<=1:
        return L
    middle = len(L)>>1
    left = L[:middle]
    right = L[middle:]
    msort_list(left)
    msort_list(right)
    merge_list(left,right,L)
    return L

msort_list(L)
print(L)
print(len(L))

#횟수만큼 출력
ret=[]
for i in range(0,len(L)):
    for j in range(0,L[i][1]):
        ret.append(L[i][0])
print(ret)
    