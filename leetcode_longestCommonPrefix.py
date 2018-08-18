class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        tmp = strs[0]
        res = 0
        for i in range(0,len(tmp)):
            for j in range(1, len(strs)):
                if strs[j][0:i+1] != tmp[0:i+1]:
                    return tmp[0:res]
            res = i+1
        return tmp




print(Solution().longestCommonPrefix(["a","b","car"]))