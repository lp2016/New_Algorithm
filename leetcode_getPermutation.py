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
    def getPermutation(self, n,k):
        # write code here
        self.L=n
        self.k=k
        if self.L == 0:
            return []
        else:
            self.data =[str(i) for i in range(1,n+1)]
            self.used = [False] * self.L
            self.result = [0] * self.L
            self.PermutationHelper(1)
            return self.re[k-1]
    def PermutationHelper(self,level):
        if level==self.L+1:
            self.re.append(''.join(self.result))
            return
        if len(self.re) == self.k:
            return
        for i in range(0,self.L):    #在每一层需要遍历全部元素
            if len(self.re)==self.k:
                return
            if not self.used[i]:
                self.result[level-1]=self.data[i]
                self.used[i]=True
                self.PermutationHelper(level+1)
                self.used[i]=False



print(Solution().getPermutation(4,9))
