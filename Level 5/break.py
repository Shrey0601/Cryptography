import os
import random


def ascii2e(a):
    res= []
    for i in range(8):
        k = ord(a[2*i])-ord('f')
        k = k*16 + ord(a[2*i+1])-ord('f')
    
        res.append(k)
    return res



def e2ascii(res):
    a = ""
    for i in range(8):
        k = res[i]
        a += chr(ord('f') + k//16)
        a += chr(ord('f') + k%16)
    return a


passenc="msfhjqifisinlogrgtjsjmkumfkrjlfs" 

passw = [ascii2e("msfhjqifisinlogr"), ascii2e("gtjsjmkumfkrjlfs")]


esend =[]
for i in range(8):
    esend.append(110)

b= True

count =0
password =[]
while(count!=8):
    print(count, esend[count])

    esend[count] +=1
    esend[count] %=128
    with open ("text.txt", 'w') as f :
        f.write(e2ascii(esend))

    
    ciph = None
    os.system('./shell.sh > out.txt') 
    with open ("out.txt", 'r') as f :
        

        content = f.readlines()


        j=135
        for i in range(0,1):
            ciph = content[j].strip()
        
    # print('here2')
    if(ascii2e(ciph)[count] == passw[0][count]):
        count+=1

p1 = e2ascii(esend)
count =0
esend =[]
for i in range(8):
    esend.append(40)


password =[]
while(count!=8):
    print(count, esend[count])

    esend[count] +=1
    esend[count] %= 128
    with open ("text.txt", 'w') as f :
        f.write(e2ascii(esend))

    
    ciph = None
    os.system('./shell.sh > out.txt') 
    with open ("out.txt", 'r') as f :
        

        content = f.readlines()


        j=135
        for i in range(0,1):
            ciph = content[j].strip()
        
    # print('here2')
    if(ascii2e(ciph)[count] == passw[1][count]):
        count+=1

p2 = e2ascii(esend)
# list to string


print(''.join([chr(x)  for x in ascii2e(p1)]) + ''.join([chr(x)  for x in ascii2e(p2)])) 
# print([chr(x)  for x in ascii2e(p2)])/
