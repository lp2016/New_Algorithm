from copy import deepcopy
class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.data=matrix
        self.res=deepcopy(matrix)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                self.res[i][j]=sum(self.data[i][0:j+1])

        # for item in matrix:
        #     r=[]
        #     sumD=0
        #     for i in range(0,len(item)):
        #         sumD=sumD+item[i]
        #         r.append(sumD)
        #     self.res.append(r[:])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sumD=0
        for i in range(row1,row2+1):
            sumD=sumD+self.res[i][col2]-self.res[i][col1]+self.data[i][col1]
        return sumD




        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
t=NumMatrix( [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
t.sumRegion(2,1,4,3)