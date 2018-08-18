class Solution(object):
    #思路：以每一个数向两边扩展，注意考虑子串长度是奇数还是偶数
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        for i in range(0,len(s)):
            j=i-1
            k=i+1
            ri=s[i]
            while j >=0 and k<len(s):
                if s[j] == s[k]:
                    ri=s[j]+ri+s[k]
                else:
                    break
                j-=1
                k+=1
            if len(result)<len(ri):
                result=ri
        for i in range(0,len(s)):
            j=i
            k=i+1
            ri=""
            while j >=0 and k<len(s):
                if s[j] == s[k]:
                    ri=s[j]+ri+s[k]
                else:
                    break
                j-=1
                k+=1
            if len(result)<len(ri):
                result=ri
        return result

print(Solution().longestPalindrome("dbbbd"))