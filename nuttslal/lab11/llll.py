p=17; q=11
n=p*q; fn= (p-1) * (q-1)
e=7
d=pow (7, -1, fn)
print (f' key: {e}, {d}')
M=88
C=pow(M, e, n)
M1=pow (C, d, n)
print (f'M: {M}, C: {C}, M1: {M1}')
abc = 'abcdefghijklmnopqrstuvwxyz'
abc += abc.upper()
abc += '0123456789 !C#?$ '
st = 'How are you?'

for ch in st:
    ind = abc.index(ch)
    num = str(ind)
    if len(num) == 1:
        num = '0' + num
    print(num, end=',')
