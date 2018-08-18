#思路：动态规划 参考：https://blog.csdn.net/u012501459/article/details/46550815
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0]=="0":                   #如果开头是0，则无法编码
            return 0
        for i in range(1,len(s)):       #0的前一个数字不能使0或者大于2的数
            if s[i]=="0" and (int(s[i-1])>2 or int(s[i-1])==0):
                return 0

        dp = [1] * len(s)
        if "0" not in s:                #如果字符串中不包含0：比如“123” ,3既可以和2结合（此时等于dp[1]）又可以单独存在（此时等于dp[2]）
            for i in range(1,len(s)):
                temp = int(s[i - 1])
                if temp * 10 + int(s[i]) <= 26 :
                    dp[i] = dp[i - 1] +dp[i-2]
                else:
                    dp[i] = dp[i - 1]

            return dp[len(s)-1]

  #如果字符串中存在0，就要以0为分隔符，将字符串分割成多块，每一块按照不包含0的方法处理
        c=1
        dp = [1] * len(s)
        t=[-1]
        for i in range(1,len(s)):
            if s[i]=="0":
                t.append(i-1)
        for i in range(0,len(t)-1):
            for j in range(t[i]+2,t[i+1]):
                print(s[j-1])
                temp = int(s[j - 1])
                if temp * 10 + int(s[j]) <= 26 :
                    dp[j]=dp[j-1]+dp[j-2]
                else:
                    dp[j]=dp[j-1]
            c=c*dp[t[i+1]-1]
        return c


print(Solution().numDecodings("1"))