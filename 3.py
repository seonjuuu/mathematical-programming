#합병정렬(2,3번이용)
def merge(L, R, B):
    nleft = len(L)
    nright = len(R)
    i=0
    l=0
    r=0
    while l<nleft and r<nright:
        if L[l]< R[r]:
            B[i] = L[l]
            i = i+1
            l = l+1
        else:
            B[i] = R[r]
            i=i+1
            r=r+1
    while l<nleft:
        B[i] = L[l]
        i=i+1
        l=l+1
    while r<nright:
        B[i] = R[r]
        i=i+1
        r=r+1

def msort(B):
    nlen = len(B)
    if nlen <=1:
        return B
    middle = nlen>>1
    L = B[:middle]
    R = B[middle:]
    msort(L)
    msort(R)
    merge(L, R, B)
    return B

##2
# 두 배열의 원소 교체
def max_A(A,B,k):
    msort(A)
    msort(B)
    
    B = B[::-1] #역순(큰수부터)
    
    for i in range(0,k):
        if A[i]<B[i]:
            A[i]=B[i]
        else:          #A의 원소가 더 크다면 어짜히 다음 B의 원소도 A보다 작음       
            break
    return sum(A)

A = [1,2,5,4,3]
B = [5,5,6,6,5]   
print(max_A(A,B,3))


##3
#최대인 수열의 합 구하기
L=[-1,2,1,3]
L=msort(L)
left = 0
right = len(L)-1
total = 0
while left<right:
    if L[left]<1 and L[left+1]<1 :  #음수끼리의 곱(0도 포함)
         total = total=L[left]*L[left+1]
         left = left+2
    else:
        break
    
while right>0 :
    if L[right] > 1 and L[right-1] > 1: #양수끼리의 곱(맨 뒤에서부터)
        total = total+L[right]*L[right-1]
        right = right-2
    else:
        break

for i in range(left, right+1):     #남은 수들 합(rigth+1까지)
    total = total+L[i]
    
print(total)

'''
#1번
##3주차(성적이 낮은 학생 순서대로 출력하기
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
    Lcpy = []
    for i in L:
        Lcpy.append(i)
        
    if len(Lcpy)<=1:
        return L
    middle = len(Lcpy)>>1
    left = Lcpy[:middle]
    right = Lcpy[middle:]
    msort(left)
    msort(right)
    merge(left,right,Lcpy)
    return Lcpy

n = int(input("N:"))
Name = []
S = [] #score
for i in range(0,n):
    a,b = input().split()
    Name.append(a)
    S.append(b)
    
Sprime = msort(S)
print("S.unsorted:",S)
print("S.sorted:",Sprime)

Nprime=[]
for i in Sprime:
    for j in range(0,len(S)):
        if i==S[j]:
            idx = j
    Nprime.append(Name[idx])
    print(Name[idx],end=" ")
'''