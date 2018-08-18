#思路：动态规划
#dp[i]为前i个字符是否可以拆分成字典中的字符
#如果dp[i-1]可以拆分成，并且s[i-1:i]在字典中
#或者dp[i-2]可以拆分成，并且s[i-2:i]在字典中
#....
#或者dp[0]可以拆分成，并且s[1:i]在字典中
#或者s[0:i]在字典中
#所以dp[i]与(dp[i-1],dp[i-2],dp[i-3]....有关
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d={}
        for i in range(len(wordDict)):
            d[wordDict[i]]=1
        dp=[False]*len(s)
        if s[0] in d:
            dp[0]=True
        if len(s)==1:
            return dp[0]

        if s[0:2] in d or (s[0] in d and s[1] in d):
            dp[1]=True


        for i in range(2,len(s)):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j+1:i+1] in d:
                    dp[i]=True
            if s[0:i+1] in d:
                dp[i]=True
        return dp[len(s)-1]


print(Solution().wordBreak("ab",  ["b"]))
