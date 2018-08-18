import numpy as np
class Solution:
    def __init__(self):
        self.N=0
        self.queens=[]
        self.res=[]
    def place(self,m,n):
        if sum(self.queens[:,n])>0:
            return False
        if sum(self.queens[m]) >0:
            return False
        i=m-1
        j=n+1
        while i>=0 and j<self.N:  #右上是否有元素
            if self.queens[i][j]:
                return False
            i-=1
            j+=1
        i = m + 1
        j = n - 1
        while i < self.N and j >=0:  # 左下是否有元素
            if self.queens[i][j]:
                return False
            i += 1
            j -= 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >=0:  # 左上是否有元素
            if self.queens[i][j]:
                return False
            i -= 1
            j -= 1
        i = m + 1
        j = n + 1
        while i <self.N and j <self.N:  # 右下是否有元素
            if self.queens[i][j]:
                return False
            i += 1
            j += 1
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.N=n
        self.queens=np.zeros([n,n])
        self.solveNQueensHelper(0)
        result=[]
        for item in self.res:
            rr=[]
            for i in item:
                s=""
                for j in i:
                    if j==0:
                        s=s+"."
                    else:
                        s=s+"Q"
                rr.append(s)
            result.append(rr)
        return result

    def solveNQueensHelper(self,n):
        if n == self.N:
            self.res.append(self.queens.copy())
            return
        else:
            for j in range(0,self.N):
                if self.place(n,j):
                    self.queens[n][j]=1
                    self.solveNQueensHelper(n+1)
                    self.queens[n][j]=0
print(Solution().solveNQueens(4))




