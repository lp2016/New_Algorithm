class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.split()
        return len(res)



print(Solution().countSegments("a"))
