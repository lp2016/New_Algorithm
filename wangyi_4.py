n=input("")
s=input("")
s1=s.split(" ")
l=len(s1)
k=l-1
while k >= 0:
    print(s1[k])
    k = k - 2
if l % 2 == 0:
    k = 0
else:
    k = 1
while k < l:
    print(s1[k])
    k = k + 2



