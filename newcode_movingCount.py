# -*- coding:utf-8 -*-
#思路：回溯法，感觉输入dfs，深度优先搜索，满足条件就继续搜，一个点被遍历过之后就置标志位为1
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold<0:
            return 0
        visit=[[ 0 for j in range(cols)] for i in range(rows)]
        count=[0]
        visit[0][0]=1
        self.movingCountHelper(0,0,threshold,visit,rows,cols,count)
        return count[0]
    def movingCountHelper(self,row,col,threshold,visit,m,n,count):
        row_sum=sum(map(int,list(str(row))))
        col_sum=sum(map(int,list(str(col))))
        count[0] += 1
        if col>0 and not visit[row][col-1] and (sum(map(int,list(str(col-1))))+row_sum)<=threshold:
            visit[row][col - 1]=1
            print(row,col-1)
            self.movingCountHelper(row,col-1,threshold,visit,m,n,count)
        if col<n-1 and not visit[row][col+1] and (sum(map(int,list(str(col+1))))+row_sum)<=threshold:
            visit[row][col +1]=1
            print(row, col+1)
            self.movingCountHelper(row,col+1,threshold,visit,m,n,count)
        if row>0 and not visit[row-1][col] and (sum(map(int,list(str(row-1))))+col_sum)<=threshold:
            visit[row-1][col]=1
            print(row-1, col)
            self.movingCountHelper(row-1,col,threshold,visit,m,n,count)
        if row<m-1 and not visit[row+1][col] and (sum(map(int,list(str(row+1))))+col_sum)<=threshold:
            visit[row+1][col]=1
            print(row+1, col)
            self.movingCountHelper(row+1,col,threshold,visit,m,n,count)
        return
print(Solution().movingCount(5,10,10))



