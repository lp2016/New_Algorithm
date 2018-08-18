class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 0
        maxD = 0
        d = {}
        for i in range(0,len(s)):
            if s[i] in d:
                maxD = max(maxD, i - left)
                left += 1
                d.clear()
                d[s[i]] = 1
            else:
                d[s[i]] = 1
        return max(maxD,i + 1 - left)
print(Solution().lengthOfLongestSubstring("dvdf"))

