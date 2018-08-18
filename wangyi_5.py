s=input("")
s1=s.split(" ")
x,f,d,p=int(s1[0]),int(s1[1]),int(s1[2]),int(s1[3])
if f <=d//x:
    day=f+(d-f*x)//(x+p)
else:
    day=d//x
print(day)