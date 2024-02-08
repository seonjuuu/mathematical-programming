#순차탐색
def linear_search(L,n):
    for i in range(0,len(L)):
        if L[i]==n:
            return i
    return -1

L = [9,8,1,2,7,3,6,4,5]
print(linear_search(L,3))

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


L=[]
for i in range(0,30):
    L.append(i)
    
print("Binary search 14?:",Binary_search(L,14))
print("Binary_search 45?:",Binary_search(L,45))

#보간탐색
def Inter_Search(L,n):
    low = 0
    high = len(L)-1
    
    while(n>=L[low] and n <= L[high] and low<=high):
        x = (high-low)*(n-L[low])/(L[high]-L[low])
        x = int(x)
        
        if L[x] < n :
            low = x+1
        elif L[x] > n :
            high = x-1
        else:
            return x
    return -1

print("Inter_Search 19?",Inter_Search(L,19))
print("Inter_Search 43?",Inter_Search(L,43))


        