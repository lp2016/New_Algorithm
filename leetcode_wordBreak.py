#思路：动态规划
#dp[i]表示前i个字符是否可以被空格拆分为一个或多个在字典中出现的单词
#显然，dp[i]取值取决于{(dp[i-1],s[i:i+1] in),(dp[i-2],s[i-1:i+1]),...,(dp[0],s[1:i+1]) }中是否有取值为true的，
# 也就是说在确定dp[i]的取值时，需要遍历dp[0:i-1]，所以时间复杂度为O(n^2)。
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
        temp=""
        for i in range(0,len(s)):
            temp=temp+s[i]
            if temp in d:
                if i == len(s)-1:
                    return True
                tt=self.wordBreakHelper(s[i+1:],d)
                if tt:
                    return True
        return False
    def wordBreakHelper(self,s,d):
        temp = ""
        for i in range(0, len(s)):
            temp = temp + s[i]
            if temp in d:
                if i == len(s)-1:
                    return True
                tt=self.wordBreakHelper(s[i + 1:],d)
                if tt:
                    return True

print(Solution().wordBreak("applepenapple",  ["apple", "pen"]))
