import random
import numpy as np
key = "4312567"
str1 = "attackpostponeduntiltwoamxyz"

def rf(str1, key):
    # deckey = ""
    # col = np.array(list(key))
    c = len(key); c1 = len(str1)
    c2 = (c-c1%c)%c; str1+=" " *c2
    c1=len(str1)
    arr = np.array(list(str1))

    newarr = arr.reshape(c1//c,c)
    print(newarr)
    str2="";str3=""
    for i in range(1,len(key) + 1):
        index = key.index(str(i))
        str3+=str2.join(newarr[:,index])
    print("dkey", key,str3)
    return str3
st=rf(str1,key)
print(st)