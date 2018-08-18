class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        if m == 1:
            return False
        for i in range(0, m):
            if i == m // 2:
                return False
            if s[0:i + 1] * (m//(i+1)) == s:
                    return True
        return False

print(Solution().repeatedSubstringPattern("ababcabc"))
