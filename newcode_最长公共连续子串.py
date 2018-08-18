def LongestSubstr(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[ 0 for j in range(n)] for i in range(m)]
    maxd = 0
    for i in range(m):
        if str1[i] == str2[0]:
            dp[i][0] = 1
            maxd = 1
    for j in range(n):
        if str2[j] == str1[0]:
            dp[0][j] = 1
            maxd = 1

    for i in range(1,m):
        for j in range(1,n):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > maxd:
                    maxd = dp[i][j]
    return maxd

s1 = input()
s2 = input()
if len(s1) == 0 or len(s2) == 0:
    print(0)
else:
    print(LongestSubstr(s1,s2))






