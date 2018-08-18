s=raw_input("")
d={s[0]:1}
c=1
for i in range(1,len(s)):
    if not d.get(s[i]):
        d[s[i]]=1
        c+=1
        if c >2:
            print(0)
            break
if c==1:
    print(1)
if c==2:
    print(2)