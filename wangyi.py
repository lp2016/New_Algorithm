s=input("")
s1=s.split(" ")
n,k=int(s1[0]),int(s1[1])
c=0
for x in range(k,n):
   c=c+n-x
print(c)