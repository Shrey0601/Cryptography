inv_perm= [
 57, 49, 41, 33, 25, 17, 9, 1,
 59, 51, 43, 35, 27, 19, 11, 3,
 61, 53, 45, 37, 29, 21, 13, 5,
 63, 55, 47, 39, 31, 23, 15, 7,
 58, 50, 42, 34, 26, 18, 10, 2,
 60, 52, 44, 36, 28, 20, 12, 4,
 62, 54, 46, 38, 30, 22, 14, 6,
 64, 56, 48, 40, 32, 24, 16, 8
]

perm2 = [
  14, 17, 11, 24,  1, 5,
  3, 28 ,15,  6, 21, 10,
  23, 19, 12,  4, 26, 8,
  16,  7, 27, 20, 13, 2,
  41, 52, 31, 37, 47, 55,
  30, 40, 51, 45, 33, 48,
  44, 49, 39, 56, 34, 53,
  46, 42, 50, 36, 29, 32
]

ipermute = [
40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25 ]

ebox = [
  32, 1, 2, 3, 4, 5,
  4, 5,6, 7, 8, 9,
  8, 9, 10, 11, 12, 13,
  12, 13, 14, 15, 16, 17,
  16, 17, 18, 19, 20, 21,
  20, 21, 22, 23, 24, 25,
  24, 25, 26, 27, 28, 29,
  28, 29, 30, 31, 32, 1
]

P = [
  16, 7, 20, 21,
  29, 12, 28, 17,
  1, 15, 23, 26,
  5, 18, 31,10,
  2, 8, 24, 14,
  32, 27, 3, 9,
  19, 13, 30, 6,
  22, 11, 4, 25,
]

inverse_permutation = [
	9, 17, 23, 31,
	13, 28, 2, 18,
	24, 16, 30, 6,
	26, 20, 10, 1,
	8, 14, 25, 3,
	4, 29, 11, 19,
	32, 12, 22, 7,
	5, 27, 15, 21,
]

Sbox = [
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

key_sched = [ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

KEY_SCHED = []

for i in range(16):
    ls = []
    for j in range(48):
        ls.append(-1)
    KEY_SCHED.append(ls)

def generate_key(type, key, rounds):
    for i in range(rounds):
        for j in range(key_sched[i]):
            lbegin = key[0]
            rbegin = key[28]
            for k in range(27):
                key[k] = key[k+1]
                key[k+28] = key[k+29]
            key[27] = lbegin
            key[55] = rbegin
        order = 0
        if type == 'encrypt':
            order = rounds - i - 1
        else:
            order = i
        for j in range(48):
            KEY_SCHED[order][j] = key[perm2[j]-1]

def unpack(packed, binary):
    for i in range(8):
        k = packed[i]
        for j in range(8):
            binary[i*8 + j] = ( k >> ( 7 - j) ) & 1
    return binary

def pack(packed, binary):
    for i in range(8):
        k = 0
        for j in range(8):
            k = ( k << 1 ) + binary[i*8 + j]
        packed[i] = k
    return packed
        
def des(inp, out1, rounds, flag):
    input = [0]*64
    input = unpack(inp, input)
    input_block = [0]*64
    temp = [0]*32
    set_key = [0]*48

    for i in range(64):
        input_block[i] = input[inv_perm[i]-1]
    
    for i in range(rounds):

        for j in range(48):
            set_key[j] = input_block[ebox[j]-1] ^ KEY_SCHED[i][j]
    
        for j in range(8):
            out = set_key[6*j]
            out = out << 1 | set_key[6*j+5]
            out = out << 1 | set_key[6*j+1]
            out = out << 1 | set_key[6*j+2]
            out = out << 1 | set_key[6*j+3]
            out = out << 1 | set_key[6*j+4]

            out = Sbox[j][out]

            temp[4*j] = out >> 3 & 1
            temp[4*j+1] = out >> 2 & 1  
            temp[4*j+2] = out >> 1 & 1
            temp[4*j+3] = out & 1

        for j in range(32):
            out = input_block[j]
            if flag == 'e':
                input_block[j] = input_block[j+32] ^ temp[P[j]-1]
            else:
                input_block[j] = input_block[j+32] ^ temp[inverse_permutation[j]-1]
            input_block[j+32] = out
        
    for i in range(64):
        input[i] = input_block[ipermute[i]-1]
    
    out1 = pack(out1, input)

rounds = 6
type = 'encrypt'

# key = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1]

# plain = [179, 53, 98, 20, 243, 178, 255, 185]

def tobyte(inp, out):
    for i in range(int(len(inp)/2)):
        out[i] = int(ord(inp[2*i]) - ord('f')) * 16 + (ord(inp[2*i + 1]) - ord('f'))
    return out

def tostr(out):
    ans = ['a']*16
    for i in range(8):
        offset = out[i]
        ans[2*i] = chr(ord('f') + int(offset/16))
        ans[2*i+1] = chr(ord('f') + int((offset%16)))
    finalans = ""
    for c in ans:
        finalans += c
    return finalans

def tolist(key):
    list_key = []
    for c in key:
        list_key.append(int(c))
    return list_key

f = open(r"keys.txt")
lines = f.readlines()
lines = [line[:-1] for line in lines]

pl = "ffffffffffffffff"
ct = "gghrsfllrpqpfunm"

inp = [0]*100
inp = tobyte(pl, inp)
cip = [0]*100
type = 'decrpyt'

cnt = 0

for keys in lines:
    cnt += 1
    keys = tolist(keys)
    generate_key(type, keys, rounds)
    des(inp, cip, rounds, 'e')
    ans = tostr(cip)
    if(ans == ct):
        break

print("Found: " + str(lines[cnt-1]))