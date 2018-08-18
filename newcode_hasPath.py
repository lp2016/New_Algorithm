# -*- coding:utf-8 -*-
#解题思路：回溯法
#首先在矩阵中找到路径path的第一个元素，然后判断当前元素的左右上下 中的某一个元素是否是path的下一个元素，
#如果是 把这个元素设置为当前元素，继续递归
import numpy as np
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        c=0
        data=[[0 for i in range(cols)] for i in range(rows)]      #掌握二维数组的创建方法
        visit =[[0 for i in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                data[i][j]=matrix[c]
                c+=1
        for i in range(rows):
            for j in range(cols):
                if path[0]== data[i][j]:
                    visit[i][j]=1
                    if self.hasPathHelper(i,j,data,path,0,visit,rows,cols):
                        return True
                    visit[i][j] = 0
        return False

    def hasPathHelper(self,row,col,data,path,c,visit,m,n):
        if c==len(path)-1:
            return True
        if col>0 and data[row][col-1]==path[c+1] and not visit[row][col-1]:
            visit[row][col-1]=1
            if self.hasPathHelper(row,col-1,data,path,c+1,visit,m,n):
                return True
            visit[row][col - 1] = 0
        if col<n-1 and data[row][col+1]==path[c+1] and not  visit[row][col+1]:
            visit[row][col+1]=1
            if self.hasPathHelper(row,col+1,data,path,c+1,visit,m,n):
                return True
            visit[row][col +1] = 0
        if row>0 and data[row-1][col]==path[c+1] and not visit[row-1][col]:
            visit[row-1][col]=1
            if self.hasPathHelper(row-1,col,data,path,c+1,visit,m,n):
                return True
            visit[row-1][col]=0
        if row<m-1 and data[row+1][col]==path[c+1] and (not visit[row+1][col]):
            visit[row+1][col]=1
            if self.hasPathHelper(row+1,col,data,path,c+1,visit,m,n):
                return True
            visit[row+1][col]=0
        return False




print(Solution().hasPath("abcesfcsadee",3,4,"abcb"))



