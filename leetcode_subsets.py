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
    def subsets(self, nums):
        # write code here
        self.L=len(nums)
        if self.L == 0:
            return []
        else:
            self.data =nums
            self.PermutationHelper(1,0)
            self.re.append([])
            return self.re

    def PermutationHelper(self, level,tmp):
        if level == self.k:
            return
        for i in range(tmp,self.L):    #在每一层需要遍历全部元素
            self.result.append(self.data[i])
            self.re.append(self.result.copy())
            self.PermutationHelper(level + 1,i+1)
            del self.result[-1]












print(Solution().subset([-1,2,3]))
