# -*- coding:utf-8 -*-
#思路：利用字典，key表示数组中的值，value代表这个值出现了几次
#      遍历 数组，验证每一个元素，如果该元素在字典中已经存在，则以这个元素为key的value加1
#      否则，这个元素是第一次出现，将这个元素为key的value置为1.
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        L=len(numbers)
        if L==0:
            return 0
        if L==1:
            return numbers[0]
        numbers=map(str,numbers)
        result={}
        for item in numbers:
            if result.get(item):
                result[item]+=1
                if result[item] > L//2:
                    return int(result[item])
            else:
                result[item]=1
        return 0
print(Solution().MoreThanHalfNum_Solution([1]))