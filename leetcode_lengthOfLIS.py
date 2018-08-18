#思路：动态规划，时间复杂度O(n^2)。切记：不要添加无关的打印语句。。。，不然会超时
#dp[i]表示以第i个数为结尾的序列的长度
#显然，dp[i]的值取决于(dp[i-1],dp[i-2],...,dp[0])中最大的且满足nums[i]大于nums[j],j=i-1,i-2,...,0.
#所以时间复杂度为O(n^2)
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        dp=[1]*len(nums)
        dp[0]=1
        res=0
        for i in range(1,len(nums)):
            maxD=0
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    maxD=max(maxD,dp[j])
            dp[i]=maxD+1
            res=max(res,dp[i])
        return res
print(Solution().lengthOfLIS( [10,9,2,5,3,7,101,18]))