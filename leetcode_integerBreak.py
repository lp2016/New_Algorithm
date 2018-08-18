#思路：动态规划
#dp[i]表示数字i可以获得的最大乘积
#dp[i]=max(dp[i-j]*j,)   j=2,3,...,i-2
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[2] = 1
        if n==2:
            return dp[2]
        dp[3] = 2
        if n==3:
            return dp[3]
        dp[4]=4
        if n==4:
            return dp[4]
        dp[5]=6
        if n==5:
            return dp[5]
        dp[6]=9           #必须写到6，因为dp[6]不满足转移方程
        if n==6:
            return dp[6]
        for i in range(7,n+1):
            maxD = 0
            for j in range(i-2,1,-1):
                maxD=max(maxD,dp[j]*(i-j))      #转移方程
            dp[i]=maxD
        return dp[n]
Solution().integerBreak(2)

