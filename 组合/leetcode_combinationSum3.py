class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        else:
            res = []
            self.combinationSum3Helper(k, n, 1, [], res, 0)
            return res

    def combinationSum3Helper(self, k, n, start, path, res, sumD):
        for i in range(start,10):
            sumD += i
            path.append(i)
            if sumD == n and len(path) == k:
                res.append(path[:])
            if sumD < n or len(path) < k:
                self.combinationSum3Helper(k, n, i+1, path, res, sumD)
            path.pop()
            sumD -= i

print(Solution().combinationSum3(3,9))


