from functools import cmp_to_key,reduce
class Solution:
    def PrintMinNumber(self, nums):
        # write code here
        if len(nums)== 0:
            return ""
        numbers=map(str,nums)
        numbers=sorted(numbers,key=cmp_to_key(lambda x,y:int(x+y)-int(y+x)))
        result=reduce(lambda x,y:x+y,numbers)
        result=''.join(result)
        return result
print(Solution().PrintMinNumber([3,32,321]))