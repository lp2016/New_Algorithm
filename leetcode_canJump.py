#思路：贪心算法
#利用变量far保存在当前位置所能到达的最远位置
# 如果nums[i] 大于far，则far赋值为far
# 如果出现far =1的情况，说明无法到达最后一个位置
class Solution:

    def canJump(self, nums):
        if len(nums) == 0 :
            return False
        if len(nums) == 1:
            return True
        far = 0
        if nums[0] == 0:
            return False
        for i in range(0,len(nums)-1):
            far -= 1
            if nums[i] > far:
                far = nums[i]
            if far == 0:
                return False
        if far >= 1:
            return True
        return False
    def canJump2(self, nums): #这种方法只能通过73/75，然后超时
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        dp = [0]*len(nums)
        if nums[0] >= 1:
            dp[1] = 1
        for i in range(2,len(nums)):
            for j in range(0,i):
                if nums[j] >= (i - j) and dp[j] == 1:
                    dp[i] = 1
        print(dp)
        if dp[len(nums)-1] == 1:
            return True
        return False
print(Solution().canJump([0,2,3]))
