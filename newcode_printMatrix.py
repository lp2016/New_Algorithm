# -*- coding:utf-8 -*-
#思路： 利用6个变量记录行列信息，包括：
#row_upper_bound：记录最大行数
# row_lower_bound：记录最小行数
# col_upper_bound：记录最大列数
# col_lower_bound：记录最小列数
# row_cur：记录当前遍历到了哪一行
# col_cur=：记录当前遍历到了哪一列
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        m=len(matrix)
        n=len(matrix[0])
        row_upper_bound=m
        row_lower_bound=0
        col_upper_bound=n
        col_lower_bound=0
        row_cur=0
        col_cur=-1
        count=0
        while count <m*n:
            for j in range(col_lower_bound, col_upper_bound):
                count+=1
                res.append(matrix[row_cur][j])
                col_cur += 1
            row_lower_bound += 1
            if count == m*n:
                break
            for i in range(row_lower_bound, row_upper_bound):
                count+=1
                res.append(matrix[i][col_cur])
                row_cur += 1
            col_upper_bound -= 1
            if count == m*n:
                break
            for j in range(col_upper_bound - 1, col_lower_bound - 1, -1):
                count+=1
                res.append(matrix[row_cur][j])
                col_cur -= 1
            row_upper_bound -= 1
            if count == m*n:
                break
            for i in range(row_upper_bound - 1, row_lower_bound - 1, -1):
                count+=1
                res.append(matrix[i][col_cur])
                row_cur -= 1
            col_lower_bound += 1
        return res
print(Solution().printMatrix([[1]]))





