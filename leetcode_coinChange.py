#思路：动态规划，零钱兑换问题
#转换成背包问题：相当于是完全背包问题，每种重量的物品有无限个（在这里每一种面额的零钱都有无限个）
#所以：可以转换成装满背包需要的物品件数最少
#物品重量：不同面额的零钱
#物品价值：都是1
#背包重量：需要兑换的金额

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        W = amount
        maxD = float("Inf")   #在这里先用一个变量将float("Inf")保存起来，不然如果每次使用maxD的时候都用float("Inf")会超时
        F = [maxD] * (W + 1)
        F[0] = 0        #表示兑换0元需要的硬币个数为0
        weight = coins[:]
        value = [1] * len(coins)

        for i in range(0, len(weight)):
            for v in range(weight[i], W + 1):
                if F[v - weight[i]] < maxD:
                    F[v] = min(F[v], F[v - weight[i]] + value[i])
        if F[-1] == maxD:
            return -1
        return F[-1]

    def coinChange2(self, coins, amount):
        if amount == 0:
            return 0
        mind = 99999         #注意设置成float("Inf")会比较慢
        dp = [mind]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i < j :
                    continue
                if dp[i] > dp[i-j] + 1:           #注意；此处利用dp[i] = min(dp[i],dp[i-j]+1)替换的话会超时。。。
                    dp[i] = dp[i-j] + 1

        if dp[amount] == mind:
            return -1
        return dp[amount]

print(Solution().coinChange2([1,2147483647],2))


