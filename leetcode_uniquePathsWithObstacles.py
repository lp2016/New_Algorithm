#不同路径II
#解题思路：动态规划
#          与不同路径I原理基本一致
#          不同点：本题，如果（i，j）位置有障碍，那么通过（i，j）的路径数为0
#                   否则，同不同路径I（走到（i,j）位置的路径=走到（i-1,j）位置的路径数+走到（i,j-1）位置的路径数）
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        if n==1:
            if sum(obstacleGrid[0])>0:
                return 0
            else:
                return 1
        if m==1:
            if sum([x[0] for x in obstacleGrid])>0:
                return 0
            else:
                return 1
        data = [[1 for i in range(0, m)] for j in range(0, n)]
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]==1:
                    data[i][j]=0
        for j in range(m):
            if obstacleGrid[0][j]==1:
                for k in range(j,m):
                    data[0][k]=0
        for j in range(n):
            if obstacleGrid[j][0]==1:
                for k in range(j,n):
                    data[k][0]=0
        for i in range(1,n):
            for j in range(1,m):
                if data[i][j]:
                    data[i][j]=data[i][j-1]+data[i-1][j]
        return data[n-1][m-1]

print(Solution().uniquePathsWithObstacles([[0],[1]]))