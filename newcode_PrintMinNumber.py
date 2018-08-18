# -*- coding:utf-8 -*-
#思路：回溯法，全排列问题：超时
class Solution:
    def __init__(self):
        self.L=0
        self.data=[]
        self.used=[]   #标志某一个元素是否被访问过
        self.result=[]  #记录单个结果
        self.re=set()   #利用set记录全部结果，可去重
        self.minD=float('Inf')

    def largestNumber(self, nums):
        # write code here
        self.L=len(nums)
        if self.L == 0:
            return ""
        else:
            self.data = nums
            self.used = [False] * self.L
            self.result = [0] * self.L
            self.PermutationHelper(1)
            return str(self.minD)
    def PermutationHelper(self,level):
        for i in range(0,self.L):    #在每一层需要遍历全部元素
            if not self.used[i]:
                self.result[level-1]=self.data[i]
                self.used[i]=True
                if level!=self.L:
                    self.PermutationHelper(level+1)
                else:
                    if ''.join(map(str,self.result)).lstrip('0'):
                        self.minD=min(self.minD,int(''.join(map(str,self.result))))
                    else:
                        self.minD=0

                self.used[i]=False


print(Solution().largestNumber([1,2,3,4,5,6,7,8,9,0]))

