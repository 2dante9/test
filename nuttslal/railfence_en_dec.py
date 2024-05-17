import numpy as np
key="4312567"
str1="attackpostponeduntiltwoamxyz"

def rf(str1,key):
    deckey=""
    col= np.array(list(key))
    c=len(key); c1=len(str1)
    c2=(c-c1%c)%c; str1+=" "*c2
    c1=len(str1)
    strr2="ttnaaptmtsuoaodwcoixknlypetz"
    arr = np.array(list(str1))
    arr1 = np.array(list(strr2))
    newarr = arr.reshape(c1//c, c)
    newarr1 = arr1.reshape(c,c1//c )
    newarr2=[]
    newarr2.append(newarr1[3].copy())
    newarr2.append(newarr1[2].copy())
    newarr2.append(newarr1[0].copy())
    newarr2.append(newarr1[1].copy())
    newarr2.append(newarr1[4].copy())
    newarr2.append(newarr1[5].copy())
    newarr2.append(newarr1[6].copy())
    newarr2=np.array(newarr2)
    print(newarr2)
    str2=""; str22="";   str3="";strr3=""
    for i in range(1,len(key)+1):
        index = key.index(str(i))
        str3+=''.join(newarr[:,index])
    for j in range(0,c1//c):
        strr3+=str22.join(newarr2[:,j])
    print("dkey",key,strr3)
    return str3

st=rf(str1,key)
print(st)





