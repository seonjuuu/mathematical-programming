#선택정렬
L=[4,2,1,0,5,3,6]

def sort_list_naive(L):
    nlen= len(L)
    
    for i in range(0, nlen):
        idx = i
        for j in range(i+1, nlen):
            if L[idx]>L[j]:
                idx = j
        L[i], L[idx] = L[idx], L[i]
        #print("i=",i,"L=",L)
    return L

print("sort_list_naive:",sort_list_naive(L))

#삽입정렬
L=[7,5,9,0,3,1,6,2,4,8]

def insert_sort(L):
    nlen = len(L)
    for i in range(1, nlen):
        for j in range(i, 0 , -1):
            if L[j]<L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
    return L
print("insert_sort:",insert_sort(L))

#퀵정렬
L = [8,2,5,3,9,4,7,6,1]

def partition_list(L, start, end):
    pivot = L[end]
    i = start -1
    for j in range (start, end):#end-1
        if L[j] <pivot:
            i= i+1
            L[i] , L[j] = L[j], L[i]
    i=i+1
    L[i], L[end] = L[end], L[i]
    return i

def quick_sort(L, start, end):
    if end<=start:
        return L
    pivot = partition_list(L, start, end)
    quick_sort(L, start, pivot -1)
    quick_sort(L, pivot+1, end)
    
    return L

print("quick_sort:",quick_sort(L,0,len(L)-1))

#합병정렬
B = [8,2,5,3,9,4,7,6,1]

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

def merge_sort(B):
    nlen = len(B)
    if nlen <=1:
        return B
    middle = nlen>>1
    L = B[:middle]
    R = B[middle:]
    merge_sort(L)
    merge_sort(R)
    merge(L, R, B)
    return B

print("merge_sort:",merge_sort(B))       

#시간비교
import time
import random

def rand_list(n):
    cnt=0
    L=[]
    while cnt<n:
        a = random.randrange(0,n)
        if a not in L :
            L.append(a)
            cnt=cnt+1
    return L

L=rand_list(1000)
start = time.time()
sort_list_naive(L)
end = time.time()
print(f"NAIVE sort : {end-start:.5f} sec")

L=rand_list(1000)
start = time.time()
insert_sort(L)
end = time.time()
print(f"Insert sort : {end-start:.5f} sec")

L=rand_list(1000)
start = time.time()
quick_sort(L,0,len(L)-1)
end = time.time()
print(f"Quick sort : {end-start:.5f} sec")

L=rand_list(1000)
start = time.time()
merge_sort(L)
end = time.time()
print(f"Merge sort : {end-start:.5f} sec")
