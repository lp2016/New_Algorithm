# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):    #这种方法为hash算法，但是空间复杂度为O(n)
        # write code here
        d={}
        for i in range(0,len(numbers)):
            if numbers[i] in d:
                duplication.append(numbers[i])
                return True
            else:
                d[numbers[i]]=1
        return False
#因为题目提到：数组中每一个数字都小于n
    def duplicate2(self, numbers, duplication):
        n=len(numbers)
        for i in range(n):

            if numbers[i]>n:
                duplication[0]=numbers[i]-2
                return True

s=[]
print(Solution().duplicate([2,1,3,1,4],s))
print(s)