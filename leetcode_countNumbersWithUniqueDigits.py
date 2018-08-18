#思路：直接求各个位数相同的数字，不要求各个位数不相同的数字
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):     #暴力方法，超时
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(1,10**n):
            s1=list(str(i))
            s2=set(s1)
            if len(s1)!=len(s2):
                count+=1
        return 10**n-count
    def countNumbersWithUniqueDigits2(self,n):
        if n<=1:
            return 0
        dp=[0]*(n+1)
        dp[2]=91
        if n==2:
            return 91
        for i in range(3,n+1):
            j = 1
            k = 9
            res = 1
            while j < i:
                res = res * k
                k = k - 1
                j = j + 1
            dp[i]=res*9+dp[i-1]
        return dp[n]
print(Solution().countNumbersWithUniqueDigits2(5))