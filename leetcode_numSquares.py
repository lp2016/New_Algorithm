#思路：动态规划，可以转化成背包问题
#实际上和零钱兑换问题原理一致
#目标：完全平方数的个数最少等价于所需要的硬币个数最少
from math import sqrt
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=int(sqrt(n))
        maxD=float("Inf")
        dp=[maxD]*(n+1)
        dp[0]=0       #表示：需要0个完全平方数组成和0
        for i in range(1,m+1):
            for v in range(i**2,n+1):
                dp[v]=min(dp[v],dp[v-i**2]+1)
        # print(dp)
        return dp[-1]
print(Solution().numSquares(1))