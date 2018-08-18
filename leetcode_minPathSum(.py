#思路：动态规划
#      data（i，j）位置的值=min（（i-1,j）,(i,j-1)）+grid(i,j)
#from copy import deepcopy   注意导报会极大影响时间效率
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        #data=deepcopy(grid)
        data=[[0 for j in range(m)] for i in range(n)]    #这种方法比上一行的方法时间效率高很多
        sumD=0
        for i in range(m):
            sumD+=grid[0][i]
            data[0][i]=sumD
        sumD=0
        for i in range(n):
            sumD+=grid[i][0]
            data[i][0]=sumD
        for i in range(1,n):
            for j in range(1,m):
                data[i][j]=min(data[i][j-1],data[i-1][j])+grid[i][j]
        return data[n-1][m-1]



print(Solution().minPathSum([
  [1],[3]
]))