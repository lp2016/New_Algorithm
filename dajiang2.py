s =input()
maxD = 0
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if s[j] == s[i]:
            t1=s[i:j]
            t2=s[j:j+(j-i)]
            if t1 == t2:
                maxD=max(maxD,len(s[i:j]))
print(maxD)