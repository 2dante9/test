import sys
sys.path.append('C:/Users/warlo/OneDrive/Desktop/hicheel/nuttslal/lab10') 
import Aes
Key = "cfb0ef3108d49cc4562d5810b0a9af60"

with open("C:/Users/warlo/OneDrive/Desktop/hicheel/nuttslal/lab/ofb.txt", "r") as f:
    V = f.read()

for i in range(8):
    V = Aes.AES(Key, V)
    print(V)