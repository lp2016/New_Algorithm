class Solution:
    #my solution O(n^2)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        for i in range(0,len(s)):
            l = {}
            l[s[i]]=1
            j=i+1
            L=1
            while j<len(s) and s[j] not in l  :
                l[s[j]]=1
                L=L+1
                j=j+1
            if result<L:
                result=L

        return result

    #best solution O(n)
    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        l = {}
        right=0
        left=0
        while right <len(s):
            if s[right] not in l  :
                l[s[right]]=1
                right+=1
                result = max(result, len(l))
            else:
                del l[s[left]]
                left+=1



        return result


Solution().lengthOfLongestSubstring_2("pwwkew")










