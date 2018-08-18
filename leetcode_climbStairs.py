#思路：转化为斐波那些数列问题，实质上也是一种简单的dp问题
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=[]
        f.append(0)
        f.append(1)
        f.append(2)
        for i in range(3,n+1):
            f.append(f[i-2]+f[i-1])
        return f[n]
print(Solution().climbStairs(4))

