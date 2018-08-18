#思路：动态规划
#dp[i][j]表示以（i，j）为右下角的正方形的边长。

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m=len(matrix)
        if m == 0:
            return 0
        n=len(matrix[0])

        if m == 1 or n == 1:
            if max(max(matrix)) == '1':
                return 1
            else:
                return 0

        dp=[[[0,0] for i in range(n)] for j in range(m)]
        for i in range(0,n):
            if matrix[0][i]=='0':
                dp[0][i][0]=0
                dp[0][i][1] = 0
            else:
                dp[0][i][0]=1
                dp[0][i][1] = 1
        for i in range(0,m):
            if matrix[i][0]=='0':
                dp[i][0][0]=0
                dp[i][0][1] = 0
            else:
                dp[i][0][0]=1
                dp[i][0][1] = 1

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='0':
                    dp[i][j][0]=0
                    dp[i][j][1] = 0
                else:
                #状态转移方程
                    dp[i][j][0]=min(dp[i-1][j-1][0],dp[i-1][j][0],dp[i][j-1][0])+1
                    dp[i][j][1] = min(dp[i - 1][j - 1][1], dp[i - 1][j][1], dp[i][j - 1][1]) + 1
        maxr=0
        maxc=0
        print(dp)
        for i in range(0,m):
            for j in range(0,n):
                maxr=max(maxr,dp[i][j][0])
                maxc=max(maxc,dp[i][j][1])
        return maxr*maxc
print(Solution().maximalSquare([
  ["1","0","0","1","1"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))

