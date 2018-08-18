# -*- coding:utf-8 -*-
#思路：回溯法，全排列问题
class Solution:
    def __init__(self):
        self.L=0
        self.data=[]
        self.used=[]   #标志某一个元素是否被访问过
        self.result=[]  #记录单个结果
        self.re=[]
        self.k=0
    def combine(self, n,k):
        # write code here
        self.L=n
        self.k=k
        if self.L == 0:
            return []
        else:
            self.data =[i for i in range(1,n+1)]
            self.used = [False] * self.L
            self.result = [0] * self.k
            self.PermutationHelper(1,0)
            return self.re

    def PermutationHelper(self, level,tmp):
        if level == self.k+1:
            self.re.append(self.result.copy())
            return
        for i in range(tmp,self.L):    #在每一层需要遍历全部元素
            self.result[level - 1] = self.data[i]
            self.PermutationHelper(level + 1,i+1)
            self.result[level-1]=0


    def PermutationHelper2(self, level,tmp):
        if level == self.k+1:
            self.re.append(self.result.copy())
            return
        for i in range(tmp,self.L):    #在每一层需要遍历全部元素
            self.result[level - 1] = self.data[i]
            self.PermutationHelper(level + 1,i+1)
            self.result[level-1]=0










print(Solution().combine(20,16))
