n=input("")
s=input("")
s1=s.split(" ")
for i in range(0,len(s1)):
    s1[i]=int(s1[i])
s2=sorted(s1)
d=float(s2[1])-float(s2[0])
work=True
for i in range(1,len(s2)-1):
    if float(s2[i+1])-float(s2[i]) !=d:
        work=False
        print("Impossible")
        break
    else:
        pass
if work:
    print("Possible")

