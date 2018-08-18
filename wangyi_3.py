s=input("")
if len(s)==1:
    print(1)
else:
    left = 0
    right = left
    L = 1
    l = 1
    while left < len(s) - 1 and right < len(s)-1:
        if s[right + 1] != s[right]:
            l += 1
            right += 1
        else:
            left += 1
            right = left
            l = 1
        L = max(L, l)
    print(L)




