#1
def cnt_coin(n):
    tmp = 1000-n
    L = [500,100,50,10,5,1]
    cnt = 0
    for i in L:
        cnt = cnt+(tmp//i)
        tmp = tmp%i
    return cnt

print(cnt_coin(380))

#2
def sum_cnt(S):
    tmp = (-1+(1+8*S)**(1/2))
    tmp = tmp/2
    return int(tmp)

print(sum_cnt(200))

#3
def num_com1(a,b):
    ret = mod_exp(a,b,10)
    if ret==0:
        ret=10
    return ret

def num_com2(a,b):
    #2로 나눈 나머지
    x1 = a&1
    #5로 나눈 나머지
    a5 = a%5
    r = b&3 #(a5**r)%5
    x2 = (a5**r)%5
    ret = (5*x1+6*x2)%10
    return ret

print(num_com1(7,100))
print(num_com1(9,635))
print(num_com2(7,100))
print(num_com2(9,635))
