
import random


def altobyte(input):
    out =[]
    for i in range(len(input)):
        input[i] = ord(input[i] - 'f')
    for i in range(0, len(input), 2):
        val = input[i] * 16 + input[i+1]
        out += [int(x) for x in list('{0:06b}'.format(val))]
    return out

def bytetoal(input):
    out = ""
    for i in range(0, len(input), 4):
        val = 0
        for j in range(4):
            val = val * 2 + input[i+j]
        out += chr(val + ord('f'))
    return out
def xor(a, b):
    return [a[i] ^ b[i] for i in range(len(a))]

def genInp(xoro):

    for i in range (100000):
        r = random.randint(0, 2**64) 

        inp = [int(x) for x in list('{0:064b}'.format(r))]

        out = xor(inp, xoro)
        print(bytetoal(inp))
        print(bytetoal(out))

def finalperm(input):
    #  inv of initalperm
    __fp = [
        39,  7, 47, 15, 55, 23, 63, 31,
        38,  6, 46, 14, 54, 22, 62, 30,
        37,  5, 45, 13, 53, 21, 61, 29,
        36,  4, 44, 12, 52, 20, 60, 28,
        35,  3, 43, 11, 51, 19, 59, 27,
        34,  2, 42, 10, 50, 18, 58, 26,
        33,  1, 41,  9, 49, 17, 57, 25,
        32,  0, 40,  8, 48, 16, 56, 24
    ]
    # Info Credit: pyDes

    return [input[i] for i in __fp]
# Diff = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

xoro = [0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
xoro = finalperm(xoro)
# print(xoro)

genInp(xoro)