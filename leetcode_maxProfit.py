class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        minD=prices[0]
        res=0
        for i in range(1,len(prices)):
            res=max(res,prices[i]-minD)
            minD=min(minD,prices[i])
        if res<0:
            return 0
        return res
    def maxProfit_dp(self, prices):
        if len(prices) <= 1:
            return 0
        dp=[0]*len(prices)
        dp[0]=0
        for i in range(1,len(prices)):
            dp[i]=max(dp[i-1]+prices[i]-prices[i-1],prices[i]-prices[i-1])
        print(dp)
        return max(0,max(dp))
print(Solution().maxProfit_dp([7,6,4,3,1]))

