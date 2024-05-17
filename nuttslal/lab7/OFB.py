from SDES_EXAMPLE_sdes import *

text="TTT One Nine Two"
key10='1010000010'
marray=bArray(text)
nonce='00000000'

def enc(key10, text, nonce):
    C=[]
    marray=bArray(text)
    for p in marray:
        O=SDES(key10,nonce,'en')
        lxr=logical_xor(p,O)
        nonce=O
        C.append(lxr)
    text = ''
    for i in C:
        o = int(i,2)
        text+=chr(o)
    return text



def dec(key10, text, nonce):
    C=[]
    marray=bArray(text)
    for c in marray:
        O=SDES(key10,nonce,'en')
        lxr=logical_xor(c,O)
        nonce=O
        C.append(lxr)
    text = ''
    for i in C:
        o = int(i,2)
        text+=chr(o)
    return text

b = enc(key10, text, nonce)
a = dec(key10, b, nonce)

print('enc', b)
print('dec', a)