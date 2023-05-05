Commands:

On entering level 4 screen:
go -> dive -> dive -> back -> pull -> exit
Login again and go to level 3 screen:
enter -> wave -> exit
Login again and go to the level 4 screen:
read -> password
Now we encounter the coded password.
After decrypting, we again go back to the level 4 screen:
read -> sssvhufsmq
Hence, we clear this level.

Cryptosystem: 6 round DES (Data Encryption Standard)

Analysis:

The text on the screen claims that the DES algorithm used has 6 rounds. Although there seems to be a confusion between 4,6, or 10 round DES. Clearly a 4-round DES is covered in class and is much easier and 10-round could be hard, we start with assuming that it is a 6 round DES first. (Also by the language of the statement it seems highly probable that it is a 6-round DES). 

1. Plaintext/Ciphertext Space: It is given in the text that a pair of consecutive letters represents 1 byte = 8 bits (or 1 letter = 4 bits). And in DES, there are 64 bits in one block. Hence, there should be 8 pairs (or 16 letters) in plaintext and ciphertext so as to make a total of 8x8 = 64 bits. This was further confirmed by generating a few input/output pairs.

Further, we observed that the letters in the output were only from 'f' to 'u'. These are a total of 16 possible letters, which is also expected since 4 bits can only represent 16 possibilities. We assume that the letters 'f' to 'u' are mapped to numbers 0 to 15 respectively (in both the plaintext and ciphertext).

2. Characteristic Used: We make use of the following 4-round characteristic: (405C0.., 04000.., 1/4, 04000.., 00540.., 5/128 , 00540.., 00.., 1, 00.., 00540.., 5/128, 00540.., 04000..). The total probability is around (0.0003814).
[Note that this is a part of the 5-round characteristic provided in the lecture]

3. Input/Output Generation: We first generate 10^5 input pairs using "input_gen.py". The inputs are generated such that the XOR of each pair is equal to the IP_inv(405C0000 04000000)= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], where IP_inv denotes the inverse of initial permutation IP. We then generate the output pairs corresponding to the input pairs using the script "shell.sh". The inputs and outputs are stored in "inpair.txt" and "outpair.txt" respectively.

IP_inv = [39,  7, 47, 15, 55, 23, 63, 31,
        38,  6, 46, 14, 54, 22, 62, 30,
        37,  5, 45, 13, 53, 21, 61, 29,
        36,  4, 44, 12, 52, 20, 60, 28,
        35,  3, 43, 11, 51, 19, 59, 27,
        34,  2, 42, 10, 50, 18, 58, 26,
        33,  1, 41,  9, 49, 17, 57, 25,
        32,  0, 40,  8, 48, 16, 56, 24]

4. Extracting the key for last round: This is done using "des.py" as follows:
	i) For each tuple (a,b,k), mem[(a,b,k)] is a list of all pairs (x,y) of 6 bit numbers such that x^y = b, S_k(x)^S_k(y) = a. 
[Here, S_k denotes the k numbered s-box of the last round].   
     ii) Consider one input pair i1,i2 and the corresponding output pair O1,O2. We first remove the final permuation from the outputs O1,O2 by applying its inverse. Let o1 = IP(O1), and o2 = IP(O2). 
    iii) Let (L_j,R_j) denote the XOR of the outputs after jth round of DES (for inputs i1,i2). For both these pairs, we know the output XOR (L6,R6) = o1^o2. And hence, we know R5 = L6. Also, L5 = R4 = 00540000 is known to be true with probability (0.0003814). 
[Note the difference in notation from the lectures, here L_j, R_j denote the "XOR" values for both computations on inputs i1,i2]
     iv) Since we already know the e-box, the permutation of the last round and we know that with some probability the XOR value L5 = 00540000, we can evaluate the XOR before and after the s-boxes are applied on these pairs. Let these XORs be b,a respectively.
      v) For each k from 1 to 8, we find the 6 bit key set for the corresponding s-box. We can then use "mem" to get the list mem[(a,b,k)], which is all pairs (x,y) such that x^y = b, S_k(x)^S_k(y) = a.
     vi) For each such pair of 6-bit numbers (x,y), we evaluate the XOR of x with e-box(o1[0:32]) (i.e. x^e-box(o1[0:32])), which is nothing but one of the candidates for the key set of the s-box 'S_k'. We also maintain a count of all the candidates for key. This counter for a number is incremented by 1, whenever that number is evaluated in the above described routine. 
    vii) The idea is that when this is repeated for a large number of input pairs, the number of times the correct key appears as a candidate is very high compared to other values. Following is the max-frequency 6-bit keys that we obtained for different s-boxes, and their comparision with the 2nd-highest frequency.
[Note: As mentioned in the lecture, We need approximately 20/p = 20/0.000381 = 52495 pairs in order to ensure that the round key is most frequently occurring value. And we are using 10^5 keys, which are enough.]

S Box 1 key:(1, 0, 1, 1, 0, 1)
Max Frequency: 8235
Mean Frequency: 6444.25
2nd Max Frequency: 6672

S Box 2 key:(1, 1, 1, 0, 1, 1)
Max Frequency: 8577
Mean Frequency: 6492.8125
2nd Max Frequency: 6642

S Box 3 key:(1, 0, 0, 1, 0, 1)
Max Frequency: 6509
Mean Frequency: 6288.28125
2nd Max Frequency: 6425

S Box 4 key:(0, 1, 0, 1, 0, 1)
Max Frequency: 6477
Mean Frequency: 6264.34375
2nd Max Frequency: 6440

S Box 5 key:(0, 0, 0, 0, 0, 1)
Max Frequency: 9189
Mean Frequency: 6591.78125
2nd Max Frequency: 6841

S Box 6 key:(0, 1, 0, 1, 1, 1)
Max Frequency: 8481
Mean Frequency: 6519.875
2nd Max Frequency: 6713

S Box 7 key:(0, 0, 1, 1, 1, 0)
Max Frequency: 8464
Mean Frequency: 6481.5625
2nd Max Frequency: 6715

S Box 8 key:(1, 1, 0, 1, 1, 0)
Max Frequency: 8617
Mean Frequency: 6501.625
2nd Max Frequency: 6768


There is a huge difference between the max and 2nd-highest frequencies in 6 out of 8 of the s-boxes (except S_3 and S_4). Hence, we can claim that these 6 are the correct 6-bit key sets with high probability. We now know 6x6 = 36 bits out of the 56 bits of the main key. 

5. Finding the Key: We use the key scheduling permutation to map the key bits for last round to the bits of the original key. The  original key, with the unknown bits represented as Master Key is given below:
Master Key:  [-1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 0, -1, 1, -1, 1, 0, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 0, -1, 0, 1, 0, 0, 0, 0, 0, -1, 1, 1, 1, 0, 0, 0, 1, 1, -1, 1, 0, -1, 1, 1, 0, 1, -1, 0, 1, 1]
It represents the parent of all possible keys.  These are generated on running des.py in a file keys.txt.

Now, we generate all possbile keys by doing a brute force on the remaining unknown 20 bits. We first evaluate an input output pair on the server's 6-round DES. This gives:
Input: ffffffffffffffff (000...0)
Output: gghrsfllrpqpfunm (000100010010110011010000011001101100101010111010000011111000011)

For all the 2^20 generated keys, we run the encryption scheme on the input "ffffffffffffffff". If the output matches the one given above, we stop and obtain the key. We use "find_key.py" for this, and the key found is: 
01101110010111100111101110000100000011100011010111011011
Reference was taken from the standard implementation of des to implement des algorithm's encryption decryption. 

6. Finding the Password: We perform the Decryption Scheme of the 6-round DES on the encrypted password using the key obtained above. This is done using "find_password.py".
Encrypted Password: qiiklhgjuiqhuuqoqkkpfuolsmgqfmpu
Decrypted Password: mimimimllnmkllmilsmgifififififif

The decrypted password when mapped back to letters from "f" to "u" (as the original scheme on the server), we get: mimimimllnmkllmilsmgifififififif. This password did not complete the level. On careful observation, we saw that the byte values all lie below 128. This indicated that these could be ASCII values. Mapping these to the corresponding ASCII characters and removing the extra padded zeros, we obtain the password for this level: sssvhufsmq

File Execution Flow:

1. Execute des.py which will generate keys.txt
2. Execute find_key.py 
3. Take the key obtained from the terminal and paste it in find_password.py after converting it to list using string_to_dict.py
4. Take the encrypted password and convert it to decimal using string_to_dec.py and paste it by dividing in two halves in find_password.py
5. You will get the final password on the terminal, and on truncating padded zeros, you get the final password.

Password: sssvhufsmq