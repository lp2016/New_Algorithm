s = input()
a = list(map(int,s.split()))
n = len(a)
dp = a[:]


#上面是读取输入元素到数组a，
#n是数组长度
#sumd 是返回值

sumd = 0
if n == 0:
    print(0)
if n == 1:
    print(a[0])

else:
    sumd = a[0]     #
    for i in range(1, n):        #循环从1到n - 1
        maxd = a[0]
        for j in range(0, i):    #循环从0到 i - 1
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + a[i])
        sumd = max(sumd, dp[i])
    print(sumd)


