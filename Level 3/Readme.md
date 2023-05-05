Commands: go, climb, pluck, c, c, back, give, back, back, thrnxxtzy, read

Cryptosystem: MonoAlphabetic Substitution-Permutation Cipher

Observations:

The frequency distribution of the letters in the ciphertext is similar to the one obtained in any generic substitution cipher. This led us to conclude that some form of substitution cipher was involved.
But the digraph frequencies are very low for the given text size. In a simple substitution cipher, the max frequency corresponding to 'th' should've been around 12. So there was a good possibility that a block permutation was involved along with a substitution cipher. So, we proceed with this observation. (Substitution-Permutation Cipher).

Now, we give two ways of finding the permutation by which the plaintext had been permuted. One way was that we could see that cipher text had a pattern similar to the last level. Hence it was likely that the word preceeding the cipher text nqg_vfusr_ec_wawy i.e. "lhvqpawr" is "password", which was led by the fact that the length of both the words is the same.  So, we started with block size = 3 and divided the text without spaces into blocks of this size and applied permuations on each block untill with block size =5 we got a match for word "lhvqpawr" with the word "password", so we inferred that the block size should be 5. Then we proceeded with the normal way of breaking substitution cipher and given in the code.

The second way is as follows:
We could also notice that in the given ciphertext, the single lettered words are and their surroundings are: 'pqcs y wsq', 'quw x decgqc'. We assume that these single lettered words are 'a' in plaintext. Since 'a' occurs with high frequency in English alphabet, and a block permutation is performed, we look for high frequency letters present around these single lettered words in the ciphertext. In our case, we find this letter to be 'q'. So we change 'q'->'a' in the ciphertext.

We saw that "fv xja" repeated in the text and the surrounding text differ for both occurrences. Since, there are blocks involved, and that too with a permutation, similar text would imply with high probability that they are part of identical blocks. This indicated that the block size could be 5. To further strengthen this claim, the number of letters before the first occurrence and between the two occurrences are multiples of 5. 

But we still iterate over all possible block sizes in range [2,6] to be sure.
Now, for each permutation, we modify the ciphertext according to the permutation, and then evaluate a 'sync_score' for the text.We use sync score as a guide to order the permutations we try to decrypt, which can be seen in the code attached.  This is evaluated based on how much the words in the text agree/disagree with the common words in English. The idea is that if we use a wrong permutation, the probability that the words sync with common words in all the blocks is negligible. We use sync_score to find the most favourable permutations and then try to decrypt them in that order. 
We first try the permutation with the highest sync_score, i.e. (3, 2, 4, 0, 1), with a score of 67.
We then proceeded to decode the cipher like we did for assignment 1.
Since the highest frequency letter 'q' is already chosen to be 'a', we replace the following two highest frequency elements as: (v,a) -> (e,t)
We similarly guess the maps of other letters interactively by completing the words in the ciphertext.
For guessing 'k' -> 'z', we used google to find that Zaffar was an evil wizard in a famous TV show "Aladin".
We finally can decode the complete ciphertext using the first permutation that we tried (i.e. based on sync_score). 

The final Substitution map is as follows:
1. ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z'] --> ['q', 'j', 'e', 'p', 'v', 's', 'g', 'f', 'c', 'm', 't', 'u', 'y', 'w', 'h', 'i', 'n', 'l', 'a', 'd', 'b', 'r', 'x', 'k']
2. ['j', 'x'] can be mapped to any permutation of ['o', 'z'].
3. All the uppercase letters are mapped  to the corresponding uppercase letters according to the map above. 
4. All other ASCII characters transform under the identity map.

The final Permutation map is as follows:
1. Block size = 5
2. Permutation = [1, 2, 3, 4, 5] --> [4, 5, 2, 1, 3] 

The final password for clearing the level is: the_magic_of_wand


Password: the_magic_of_wand
