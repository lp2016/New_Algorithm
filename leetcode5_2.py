class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        i=0
        while i<len(s):
            j=i+1
            c=1
            while j<len(s) and s[j] == s[i]:
                c+=1
            if c%2 ==0:
                k=c//2
                i+=k-1
            elif c>1:
                i+=1

            i+=1


        return result

print(Solution().longestPalindrome("dbbbd"))