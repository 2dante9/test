p10=[3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8=[6, 3, 7, 4, 8, 5, 10, 9]

ip8=[2, 6, 3, 1, 4, 8, 5, 7]
ep8=[4,1,2,3,2,3,4,1]
pi4=[2,4,3,1]
ip_1=[4,1,3,5,7,2,8,6]

s0=[['01','00','11','10'],
    ['11','10','01','00'],
    ['00','10','01','11'],
    ['11','01','11','10']]

s1=[['00','01','10','11'],
    ['10','00','01','11'],
    ['11','00','01','00'],
    ['10','01','00','11']]
def ip(key,st):
    s=''
    for i in key:
        s=s+st[i-1]
    return s
def logical_xor(str1, str2):
    xr=''
    for i in range(0,len(str1)):
        b='1'
        if str1[i]==str2[i]:
            b='0'
        xr=xr+b
    return xr
#row column index
def RC(str1):
    s = 0
    if str1=='01':
        s=1
    if str1=='10':
        s=2
    if str1=='11':
        s=3
    return s

def dev5(key10,b):
    key5L=key10[0:5]
    key5R=key10[5:]
    key5L=key5L[b:]+key5L[0:b]
    key5R=key5R[b:]+key5R[0:b]
    key10=key5L+key5R
    k1=ip(p8,key10)
    return k1, key10

def key(key10):
    key10=ip(p10,key10)
    k1,key10=dev5(key10,1)
    k2,key10=dev5(key10,2)
    return k1,k2

def rund(P,k):
    L=P[0:4]
    R=P[4:]
    ep=ip(ep8,R)
    ep=logical_xor(ep,k)
    
    s0r=RC(ep[0]+ep[3])
    s0c=RC(ep[1]+ep[2])
    s1r=RC(ep[4]+ep[7])
    s1c=RC(ep[5]+ep[6])

    P4=s0[s0r][s0c]
    P4+=s1[s1r][s1c]

    P4=ip(pi4,P4)
    P4=logical_xor(P4,L)
    P=R+P4
    return P

def E(key10,P):
    k1,k2=key(key10)
    P=ip(ip8,P)
    P=rund(P,k1)
    P=rund(P,k2)
    P=P[4:]+P[0:4]
    P=ip(ip_1,P)
    return P
def D(key10,P):
    k2, k1 = key(key10)
    P=ip(ip8,P)
    P=rund(P,k1)
    P=rund(P,k2)
    P=P[4:]+P[0:4]
    P=ip(ip_1,P)
    return P
def bArray(text):
    binArr=[]
    for i in text:
        p=decimalToBinary(ord(i),8)
        binArr.append(p)
    return binArr
def decimalToBinary(n,b):
    bnr=bin(n).replace("0b", "")
    bnr=bnr.rjust(b, '0') #this reverses an array.
    return bnr