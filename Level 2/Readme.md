Commands: go, back, read

Cryptosystem: Vigenere Cipher

Observations:

After entering "go", we came across a screen that asked us to count the number of lines horizontally. This had to be done while rising up after bowing down. So we counted the number of lines horizontally from in a down-up manner. This resulted in the numbers "9,2,9,2,5,5,2,2,2,1". 

Because it was told that this would help us, we tried to check if this was the key. All the numbers were less than 26. This immediately gave rise to suspicion of it being related to caesar's cipher.  So we tried these as keys one by one. "9" didn't yield good results, so we tried "2". On entering "2" we found many recognisable words in the result text like "is", "the","may", "go". There were also some four letter words for which some of their 3 letter parts were recognisable. Since "2" appeared thrice consecutively in the list of numbers, we thought of the possibility of these numbers being used one by one. So we tried using these numbers one by one for each letter. We found that initial results made sense "be wary of ..." after these numbers were finished, we repeated them again. This lead to perfectly recognisable text.

Algorithm Used:

key = "9292552221" : repeated as many times as required to match the length of the ciphertext.
count =0
for x in ciphertext:
    if(x is not letter):
        print(x)

    else:
        s= character (x - key[count%10]) # this denotes cyclic alphabetic shift by key[count%10]
        print(s)
        count +=1

Result:

Be wary of the next chamber, there is very little joy there. Speak out the password "the_cave_man_be_pleased" to go through. May you have the strength for the next chamber. To find the exit, you first will need to utter magic words there.

Password: the_cave_man_be_pleased