class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m={}
        result=[]
        for index,value in enumerate(nums):
            m[value]=index
        print(m)
        for index, value in enumerate(nums):
            key=m.get(target-value,-1)
            if key!=-1 and index !=key:
                result.append(index)
                result.append(m.get(target-value))
                return result
print(Solution().twoSum([2,2,5,6],4))