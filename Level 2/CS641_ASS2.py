a= '''Kg fcwd qh vin pnzy hjcocnt, cjjwg ku wnth nnyvng kxa cjjwg. Urfjm xwy yjg rbbufqwi "vjg_djxn_ofs_dg_rmncbgi" yq iq uqtxwlm. Oca zxw qcaj vjg tctnplyj hqs cjn pjcv ejbvdnt. Yt hkpe cjn gcnv, aqv okauy bknn ongm vt zvvgs vcpkh bqtft cjntj.'''
key = "9292552221"
count =0
for i in range(len(a)):
    if (ord(a[i])<ord('a') or ord(a[i])>ord('z')) and (ord(a[i])<ord('A') or ord(a[i])>ord('Z')):
        # check if it is a letter
        print(a[i], end="")
    else:
        b= chr(ord(a[i]))
        f = b.isupper()
        b = b.lower()
        # covert to lower case
        if f:
            print (chr((ord(b) - ord('a') - int(key[count%len(key)]))%26 + ord('A')), end="")
        else :
            print (chr((ord(b) - ord('a') - int(key[count%len(key)]))%26 + ord('a')), end="")
        # shift the letter by the key
        count +=1