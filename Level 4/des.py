import numpy as np
from itertools import product


def ebox(input):
    eTab = [31,  0,  1,  2,  3,  4,
            3,  4,  5,  6,  7,  8,
            7,  8,  9, 10, 11, 12,
            11, 12, 13, 14, 15, 16,
            15, 16, 17, 18, 19, 20,
            19, 20, 21, 22, 23, 24,
            23, 24, 25, 26, 27, 28,
            27, 28, 29, 30, 31,  0]
    # Info Credit: pyDes

    return [input[i] for i in eTab]





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


def initalperm(input):
    # flipped, inverse from finalperm
    __rfp = [57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8]


    
    return [input[i-1] for i in __rfp]


def sbox(input, k=-1):
    sTab = [
        # S1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
         0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
         4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
         15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

        # S2
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
         3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
         0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
         13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

        # S3
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
         13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
         13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
         1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

        # S4
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
         13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
         10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
         3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

        # S5
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
         14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
         4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
         11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

        # S6
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
         10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
         9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
         4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

        # S7
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
         13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
         1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
         6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

        # S8
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
         1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
         7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
         2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
    # Info Credit: pyDes
    out = []
    if (k == -1):
            for i in range(8):
                row = input[6*i]*2 + input[6*i+5]
                col = input[6*i+1]*8 + input[6*i+2]*4 + input[6*i+3]*2 + input[6*i+4]
                val = sTab[i][row*16+col]
                out += [(val & 8) >> 3, (val & 4) >> 2, (val & 2) >> 1, val & 1]
            return out
    else:
        i=0
        row = input[6*i]*2 + input[6*i+5]
        col = input[6*i+1]*8 + input[6*i+2]*4 + input[6*i+3]*2 + input[6*i+4]
        val = sTab[k-1][row*16+col]
        out += [(val & 8) >> 3, (val & 4) >> 2, (val & 2) >> 1, val & 1]
        return out
        # return [out[i] for i in range(4*(k-1), 4*k)]


def pbox(input):
    pTab = [
        15, 6, 19, 20, 28, 11,
        27, 16, 0, 14, 22, 25,
        4, 17, 30, 9, 1, 7,
        23, 13, 31, 26, 2, 8,
        18, 12, 29, 5, 21, 10,
        3, 24
    ]
    return [input[i] for i in pTab]
pTab = [
        15, 6, 19, 20, 28, 11,
        27, 16, 0, 14, 22, 25,
        4, 17, 30, 9, 1, 7,
        23, 13, 31, 26, 2, 8,
        18, 12, 29, 5, 21, 10,
        3, 24
    ]
ipTab = []
for i in range(32):
        ipTab.append(pTab.index(i))

def ipbox(input):
    #  Inverse of pbox
        
    return [input[i] for i in ipTab]


mem = None


def xor(a, b):
    return [a[i] ^ b[i] for i in range(len(a))]


if mem is None:
        mem = {}
        for k in range(1, 9):
            for i in range(2**6):
                for j in range(2**6):

                    # i1 = binary list of i
                    i1 = [int(x) for x in list('{0:06b}'.format(i))]
                    # j1 = binary list of j
                    j1 = [int(x) for x in list('{0:06b}'.format(j))]
                    # print(i1, j1)
                    if ((tuple(xor(sbox(i1, k), sbox(j1, k))), tuple(xor(i1, j1)), k) not in mem):
                        mem[(tuple(xor(sbox(i1, k), sbox(j1, k))), tuple(xor(i1, j1)), k)] = []
                    mem[(tuple(xor(sbox(i1, k), sbox(j1, k))), tuple(xor(i1, j1)), k)].append((i1, j1))

def altobyte(input):
    out =[]
    input = input.strip()
    ins=[]
    for i in range(len(input)):
        ins.append(ord(input[i]) - ord('f'))
    # print(input)
    # print(len(ins))
    for i in range(0, len(ins), 2):
        val = ins[i] * 16 + ins[i+1]
        out += [int(x) for x in list('{0:08b}'.format(val))]
        # print(len([int(x) for x in list('{0:08b}'.format(val))]))
    return out

fopen = open("inpair.txt", "r")
fopen2 = open("outpair.txt", "r")
inputs =[]

inpair =[]
outpair =[]
for line in fopen:
    inpair.append(line)
for line in fopen2:
    outpair.append(line)

freq={}
for i in range(0, len(outpair), 2):

    o1 = altobyte(outpair[i])
    o2 = altobyte(outpair[i+1])
    i1 = altobyte(inpair[i])
    i2 = altobyte(inpair[i+1])
    # print(xor (i1, i2))
    # break
    # print(o1)
    # print(o2)
    # print(len(o1))
    o1 = initalperm(o1)
    o2 = initalperm(o2)
    # print(o1)
    # print(o2)
    # break
    r6 = xor(o1, o2)[32:64]
    r5 = xor(o1, o2)[0:32]

    


    XORG = [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    XORG= XORG[32:64]
    # print("heloo",XORG)

    inputs.append((ipbox(xor(r6, XORG)), ebox(r5), ebox(o1[0:32]) ))
    
# print('hello',freq[tuple([0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])])
# print(inputs[0])
    
key = [] 
boxes = [1, 2, 5, 6, 7, 8]
    
for k in range(8):
    ki = {}

    for x in inputs:
        y = []
        y.append(x[0][4*k: 4*k+4])
        y.append(x[1][6*k: 6*k+6])
        y.append(x[2][6*k: 6*k+6])
        y = tuple(y)
        
        if((tuple(y[0]), tuple(y[1]), k+1) not in mem):
            continue
        # print(mem[(tuple(y[0]), tuple(y[1]), k+1)][0])
        # print(y)
        for yy in mem[(tuple(y[0]), tuple(y[1]), k+1)]:
            if (tuple(xor(yy[0], y[2])) not in ki):
                   ki[tuple(xor(yy[0], y[2]))] = 0
            ki[tuple(xor(yy[0], y[2]))] += 1

    # get max, avg
    maxkey = None
    # get max, second max
    mean = []
    liss = []
    
    for i in ki:
        mean.append(ki[i])
        liss.append((ki[i], i))
    
    liss.sort(reverse=True)

    if k+1 in boxes:
        for i in range(6):
            key.append(liss[0][1][i])
    
    print("S Box " + str(k+1) + " key:" + str(liss[0][1]))
    print("Max Frequency: " + str(liss[0][0]))
    print("Mean Frequency: " + str(sum(mean)/len(mean)))
    print("2nd Max Frequency: " + str(liss[1][0]))
    

    # print("max", maxkey, ki[maxkey])

key_obt = [24, 27, 21, 6, 11, 15,
13, 10, 25, 16, 3, 20,
51, 34, 41, 47, 29, 37,
40, 50, 33, 55, 43, 30,
54, 31, 49, 38, 44, 35,
56, 52, 32, 46, 39, 42]

final_key = []

for i in range(56):
    final_key.append(-1)

count = 0

for i in key:
    final_key[key_obt[count]-1] = i
    count += 1

print(final_key)

def generate_combinations(bits):
    count = bits.count(-1)
    for values in product([0, 1], repeat=count):
        result = list(bits)
        index = 0
        for i in range(len(result)):
            if result[i] == -1:
                result[i] = values[index]
                index += 1
        yield result

possible_keys = list(generate_combinations(final_key))

print(len(possible_keys))

print(len(possible_keys))

fopen3 = open("keys.txt", "w")

for keys in possible_keys:
    for bits in keys:
        fopen3.write(str(bits))
    fopen3.write("\n")

