class Solution:
    def lengthOfLongestSubstring(self,s):
        if len(s) <= 1:
            return len(s)
        times = [-1] * 256
        f = [1] * len(s)
        times[ord(s[0]) - 256] = 0
        res = 0
        for i in range(1, len(s)):
            if times[ord(s[i]) - 256] == -1:
                f[i] = f[i - 1] + 1
            else:
                d = i - times[ord(s[i]) - 256]
                if d > f[i - 1]:
                    f[i] = f[i - 1] + 1
                else:
                    f[i] = d
            times[ord(s[i]) - 256] = i
            res = max(res, f[i])
        return res

    def lengthOfLongestSubstring2(self, s):
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

