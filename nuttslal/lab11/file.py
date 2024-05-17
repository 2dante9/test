import sys
import numpy as np

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&()*+,-./\:;<=>?@[\]^_`{|}~\n\t'

file1 = open("plain.txt", "r") 
st = file1.read()
file1.close() 
if len(st) % 2 == 1:
    st = st + " "
lst = [abc.index(chr) for chr in st]

arr = np.array(lst).reshape(-1, 2)

P = [i[0] * 100 + i[1] for i in arr]

p = 73
q = 151
n = p * q
e = 11
et = (p - 1) * (q - 1)
d = pow(e, -1, et)


def myPow(a, e, n):
    result = 1
    for bit in bin(e)[2:]:
        result = (result*result) % n
        if bit == '1':
            result = (result * a) % n
    return result

def RSA(P, p, q, qw):
    C = []
    n = p * q
    e = 11
    et = (p - 1) * (q - 1)
    d = pow(e, -1, et)
    
    if qw == "en":
        for pp in P:
            C.append(myPow(pp, e, n))
    elif qw == "de":
        for cc in P:
            pp = myPow(cc, d, n)
            x1 = pp // 100
            x2 = pp % 100
            C.append(x1)
            C.append(x2) 
    return C 


def f_to_t(C):
    B = []
    for cc in C:
        x1 = cc // 100
        x2 = cc % 100
        B.append(hex(x1)[2:])
        B.append(hex(x2)[2:])
    return B


C = RSA(P
        , p, q, "en")
E = f_to_t(C)
e_message = ''.join([ind for ind in E])
file1 = open("enc.txt", "w") 
file1.write(e_message)
file1.close() 

D = RSA(C, p, q, "de")
decrypted_message = ''.join([abc[ind] for ind in D if ind < len(abc)])
file1 = open("dec.txt", "w") 
file1.write(decrypted_message)
file1.close()