from SDES_EXAMPLE_sdes import *

key10='1010000010'
text="TTT One Nine Two"
def enc(key10, text):
    marray=bArray(text)
    C=[]
    n=0
    for p in marray:
        nt=decimalToBinary(n,8)
        O=SDES(key10,nt,'en')
        lxr=logical_xor(p,O)
        C.append(lxr)
        n+=1
    txt = ''
    for i in C:
        o = int(i,2)
        txt+=chr(o)
    return txt



def dec(key10, text):
    marray=bArray(text)
    C=[]
    n=0
    for c in marray:
        nt=decimalToBinary(n,8)
        O=SDES(key10,nt,'en')
        lxr=logical_xor(c,O)
        C.append(lxr)
        n+=1
    txt = ''
    for i in C:
        o = int(i,2)
        txt+=chr(o)
    return txt

b = enc(key10, text)
a = dec(key10, b)

print('enc:', b)
print('dec', a)