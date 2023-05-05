Commands: climb, read, enter, read

Crytposystem: Substitution Cipher


Observations:

Ordered relations like preservation of readable length of words in ciphertext, organised use of quotes, full stops and punctuations suggests the use of a permutation cipher which preserves the encoding of spaces and punctuation marks. Caesar cipher and Substitution cipher are the first candidates that come to mind. It is easy to check that caesar cipher doesn't give a readable decryption for any shift. 

Further, words like "wa", "mey" appear very frequently in ciphertext. This strengthens the belief that the used cryptosystem would be a substitution cipher. 

We try performing a  frequency analysis-based attack on the system as follows:
This attack was done with the assistance of some python subroutines. The uploaded code is a python notebook that contains precise and elaborate attack steps.  

# Replacing the top three letters with the generally observed top three letters (e,t,a, respectively).
# y to e
# m to t
# a to a

# Since 'aee' is not in english. We will try replacing only the top 2 letters with (e,t respectively).

# There are only two single lettered words in english (a,I).
# Replacing the single lettered words in the given text with 'a'.
# p to a

# Replacing the digraph with highest frequency (me) with the generally observed top digraph (th).

# The first two words should be "This is". Replacing (w,a) with (i,s) respectively.

# The second word in the third line should be "in" or "is". But since "is" is already decoded, it must be "in".
# Replacing 'h' with 'n'.

# The first word in the third line should be "interest".
# Replacing 's' with 'r'.

# The third word in the first line should be "first".
# Replacing 't' with 'f'.

# The seventh word in the second line should be "nothing".
# Replacing (g,r) with (o,g) respectively.

# The last word in the fifth line should be "message".
# The first two words of the seventh line should be "digits have"
# Replacing (j,u,b) with (m,d,v) respectively.

# The sixth line should be "is a simple substitution cipher in which"
# Replacing (f,k,n,o,i) with (p,l,u,b,c) respectively.

# Gessing the rest of the words is easy.
# xou --> you
# vill --> will
# duotes --> quotes


# From the information about digit permutation given in the text, the digits are rotated by x (say):
# 8 - x = x (mod 10) => 2x = 8 (mod 10) => x = 4 (mod 5) => x = 4 or 9 (mod 10).

By entering the pass, we find that x=4 cracks the code.


These transformations result in the final text :


This is the first chamber of the caves.
As you can see, there is nothing of
interest in the chamber. Some of the later
chambers will be more interesting than
this one! The code used for this message
is a simple substitution cipher in which
digits have been shifted by 4 places.
The password is "tyRgU69diqq" without the
quotes.

Mapping:

Plaintext space refers to natural unencrypted information, readable without any decryption. 
Ciphertext refers to encrypted information produced from plain text using encryption algorithms making it secure for transferring.

In our case Cipher text and Plain text are sets of finite strings made up of ASCII characters. 
Since all of the letters are not used in the given text, map may not be unique. One such possible map is:
The mapping of characters is (plaintext to ciphertext)

[abcdefghijklmnopqrstuvwxyz] -> [poiuytrewlzkjhgfdsamnbvcxq]
[ABCDEFGHIJKLMNOPQRSTUVWXYZ] -> [POIUYTREWLZKJHGFDSAMNBVCXQ]
[0123456789] ---> [4567890123]
Rest of ASCII characters follow identity map.