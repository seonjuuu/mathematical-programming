def num_coin(N):
    L = [500,100,50,10]
    cnt = 0
    for i in L:
        cnt = cnt + (N//i) #N=1260 -> 260
        N = N%i
    return cnt

print(num_coin(1260))

def  lrg_sum(L,k,m):
    ret = 0
    cnt = 0
    L.sort()
    L=L[::-1] #L[6,...]
    while cnt<m:
        subcnt = 0
        while subcnt < k and cnt < m :
            ret = ret+L[0]
            subcnt=subcnt+1
            cnt=cnt+1
        if cnt < m :
            ret = ret+L[1]
            cnt = cnt+1
    return ret

L=[2,1,6,5,4]
print(lrg_sum(L,3,8))

def lrg_sum2(L,k,m):
    L.sort()
    L=L[::-1]
    ret = 0
    subsum = k*L[0]+L[1]
    iter = m//(k+1)      #들어가는 횟수
    ret = subsum*iter    #총 합
    cnt = m-iter*(k+1)   #횟수 s남은수
    ret = ret + cnt*L[0]
    return ret

print(lrg_sum2(L,3,8))