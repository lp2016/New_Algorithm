class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        L=len(cost)
        dp=[0]*L
        dp[0]=cost[0]
        dp[1]=cost[1]
        if L==2:
            return min(dp[0],dp[1])
        for i in range(2,L):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]

        return min(dp[L-1],dp[L-2])
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

