import sys
lines = sys.stdin.readlines()
n = int(lines[0].strip().split()[0])
k = int(lines[0].strip().split()[1])
a = list(map(int,lines[1].strip().split()))
mind = a[0]
index = 0
for i in range(1,len(a)):
    if a[i] < mind:
        mind = a[i]
        index = i
right = index
count = 0
while right < len(a) - 1:
    count += 1
    right = right + k - 1
left = index
while left > 0:
    count += 1
    left = left - k + 1
print(count-1)