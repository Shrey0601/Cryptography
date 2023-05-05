s="qiiklhgjuiqhuuqoqkkpfuolsmgqfmpu"
ans=[]
for i in range(0,len(s),2):
    x = ord(s[i]) - ord('f')
    y = ord(s[i+1]) - ord('f')
    ans.append(y + x*16)
print(ans)