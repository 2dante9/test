import sys
sys.path.append('C:/Users/warlo/OneDrive/Desktop/hicheel/nuttslal') 
import AES
V= "4c89af496176b728ed1e2ea8ba27f5a4"
Key = "cfb0ef3108d49cc4562d5810b0a9af60"

pwr=pow(2,128)
for i in range(7):
    V = AES.AES(Key, V)
    V = (int(V, 16)+1)%pwr
    V = hex(V) [2:]
    if len(V) < 33:
        V = '0'*(32-len(V)) + V
    print(V)