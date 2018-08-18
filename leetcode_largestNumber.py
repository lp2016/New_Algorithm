# -*- coding:utf-8 -*-
#思路：把所有元素都排序：利用交换排序的方法，只不过交换的条件是：如果xy>yx则x需要放在y之前
#      在这里直接调用的python的内置函数：sorted（），并且使用cmp_to_key作为sorted（）的key参数
from functools import cmp_to_key,reduce
class Solution:
    def largestNumber(self, nums):
        # write code here
        if len(nums)== 0:
            return ""
        numbers=map(str,nums)
        numbers=sorted(numbers,key=cmp_to_key(lambda x,y:int(y+x)-int(x+y)))
        result=reduce(lambda x,y:x+y,numbers)
        result=''.join(result).lstrip('0')
        return result or '0'
print(Solution().PrintMinNumber([0,0,0]))