class Solution:
    #思路：动态规划
    #三维列表：qp，qp[i][j]存储的是位置（i，j）可以到达的位置
    #三维列表：dp，dp[i][j][k]存储的是，以位置（i，j）为起始点，走k步后，依然在棋盘上的走法
    #最优子结构：
    #比如以（0,0）为起始点，（0,0）走一步可以到达的并且在棋盘上的位置是（1,2）和（2,1）
    #那么dp[0][0][k]只和dp[1][2][k-1]、dp[2][1][k-1]有关
    def knightProbability(self, N, K, r, c):

        if K==0:
            return 1.0
        qp=[[[] for i in range(N) ] for j in range(N)]
        dp=[[[0]*K for i in range(N) ] for j in range(N)]
        for i in range(N):
            for j in range(N):
                self.ad(i,j,qp,N)
        for i in range(N):
            for j in range(N):
                dp[i][j][0]=len(qp[i][j])
        for k in range(1,K):
            for i in range(N):
                for j in range(N):
                    for item in qp[i][j]:
                        dp[i][j][k] += dp[item[0]][item[1]][k - 1]
        return dp[r][c][K-1]/(8**K)

    def ad(self, i, j, qp, N):
        if i - 1 >= 0 and j - 2 >= 0:
            qp[i][j].append((i - 1, j - 2))
        if i - 2 >= 0 and j - 1 >= 0:
            qp[i][j].append((i - 2, j - 1))
        if i - 2 >= 0 and j + 1 < N:
            qp[i][j].append((i - 2, j + 1))
        if i - 1 >= 0 and j + 2 < N:
            qp[i][j].append((i - 1, j + 2))
        if i + 1 < N and j + 2 < N:
            qp[i][j].append((i + 1, j + 2))
        if i + 2 < N and j + 1 < N:
            qp[i][j].append((i + 2, j + 1))
        if i + 2 < N and j - 1 >= 0:
            qp[i][j].append((i + 2, j - 1))
        if i + 1 < N and j - 2 >= 0:
            qp[i][j].append((i + 1, j - 2))

    def knightProbability(self, N, K, r, c):  #深度优先搜索，超时
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K==0:
            return 1.0
        qp=[[[] for i in range(N) ] for j in range(N)]
        for i in range(N):
            for j in range(N):
                self.ad(i,j,qp,N)
        count=0
        if K==1:
            return len(qp[r][c])/8
        for item in qp[r][c]:
            count+=(self.dfs(item,2,K,qp))/8
        return count
    def dfs(self,item,k,K,qp):
        r=item[0]
        c=item[1]
        count=0
        print(k)
        if k==K:
            return len(qp[r][c])/8
        for item in qp[r][c]:
            count+=(self.dfs(item,k+1,K,qp))/8
        return count
    def ad(self,i,j,qp,N):
        if i-1>=0 and j-2>=0:
            qp[i][j].append((i-1,j-2))
        if i-2>=0 and j-1>=0:
            qp[i][j].append((i-2,j-1))
        if i-2>=0 and j+1<N:
            qp[i][j].append((i-2,j+1))
        if i-1>=0 and j+2<N:
            qp[i][j].append((i-1,j+2))
        if i+1<N and j+2<N:
            qp[i][j].append((i+1,j+2))
        if i+2<N and j+1<N:
            qp[i][j].append((i+2,j+1))
        if i+2<N and j-1>=0:
            qp[i][j].append((i+2,j-1))
        if i+1<N and j-2>=0:
            qp[i][j].append((i+1,j-2))









print(Solution().knightProbability2(3,1,0,0))