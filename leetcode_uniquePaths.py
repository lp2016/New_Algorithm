#不同路径I
# 解题思路：动态规划
#          其实和爬楼梯问题原理大致相同，
#          爬到第i个楼梯上的方法是爬到第i-1个楼梯上的方法和爬到第i-2个楼梯上方法的和
#          这道题：走到（i,j）位置的路径=走到（i-1,j）位置的路径数+走到（i,j-1）位置的路径数
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        data=[[1 for i in range(0,m)] for j in range(0,n) ]
        for i in range(1,n):
            for j in range(1,m):
                data[i][j]=data[i][j-1]+data[i-1][j]
        print(data)
        return data[n-1][m-1]
print(Solution().uniquePaths(3,2))


