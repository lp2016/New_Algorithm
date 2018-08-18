class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.threeSumHelper(nums,0,[],0,res,0)
        res = list(map(sorted,res))
        res2 = set()
        for item in res:
            item = map(str,item)
            res2.add(''.join(item))

        return res2

    def threeSumHelper(self, nums, level, path,sumd,res,index):
        if level == 3 :
            if sumd == 0:
                res.append(path[:])
            return
        for i in range(index,len(nums)):
            sumd += nums[i]
            path.append(nums[i])
            self.threeSumHelper(nums,level+1,path,sumd,res,i+1)
            path.pop()
            sumd -= nums[i]
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
