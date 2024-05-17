import random as rnd
q = 257
a = 101

Xa = 51
Ya = pow(a, Xa, q)

file1 = open("plain.txt", "r")
st = file1.read()
file1.close()

C = []

def enc(st, q, Ya, a):
    for ch in st:
        M = ord(ch)
        k = rnd.randrange(q)
        K = pow(Ya, k, q)
        C1 = pow(a, k, q)
        C2 = (M * K) % q
        C.append(C1)
        C.append(C2)
    return C


def dec(CT, q, Xa):
    dec_mess =""
    for i in range(0, len(CT), 2):
        C1 = CT[i]
        C2 = CT[i + 1]

        K = pow(C1, Xa, q)
        k_1 = pow(K, -1, q)
        m = (C2 * k_1) % q
        dec_mess += chr(m)

    return dec_mess


def f_to_t(C):
    B = []
    for cc in C:
        x1 = cc // 100
        x2 = cc % 100
        B.append(hex(x1)[2:])
        B.append(hex(x2)[2:])
    return B


enc_ = enc(st, q, Ya, a)
print(enc_)
print(len(enc_))

enc = f_to_t(enc_)
e_message = ''.join([ind for ind in enc])

file1 = open("enc.txt", "w")
file1.write(e_message)
file1.close()

dec_ = dec(enc_, q, Xa)
print(dec_)


file1 = open("dec.txt", "w")
file1.write(dec_)
file1.close()