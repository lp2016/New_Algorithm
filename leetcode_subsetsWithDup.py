# -*- coding:utf-8 -*-
#思路：回溯法，全排列问题
class Solution:
    def __init__(self):
        self.L=0
        self.data=[]
        self.used=[]   #标志某一个元素是否被访问过
        self.result=[]  #记录单个结果
        self.re=[]
        self.hp=set()
        self.k=0
    def subsetsWithDup(self, nums):
        # write code here
        self.L=len(nums)
        nums.sort()            #需要先排下序
        if self.L == 0:
            return []
        else:
            self.data =nums
            self.PermutationHelper(1,0)
            self.re.append([])
            return self.re

    def PermutationHelper(self, level,tmp):
        if level == self.L+1:
            return
        for i in range(tmp,self.L):    #在每一层需要遍历全部元素
            self.result.append(self.data[i])
            tmp=''.join(map(str,self.result[:]))        #防止4414 1444这种，必须加
            if  tmp not in self.hp:
                self.re.append(self.result.copy())
                self.hp.add(tmp)
            self.PermutationHelper(level + 1,i+1)
            del self.result[-1]

    # def others(self,level,tmp):
    #     if level == self.L












print(Solution().subsetsWithDup([4,4,4,1,4]))
