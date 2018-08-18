#思路：动态规划
#dp[i]定义为：前i个字符是否为t的子序列
#tmp[i]定义为：s[i]在t中的位置
#判断dp[i]是否为true，只需要判断在t[tmp[i-1]:]中能否找到s[i]，找到dp[i]则为true，找不到为false
#时间复杂度O(n^2)
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return False
        dp=[False]*len(s)
        tmp=[0]*len(s)
        for i in range(0,len(t)):
            if s[0]==t[i]:
                dp[0]=True
                tmp[0]=i
                break
        if len(s)==1:
            return dp[0]
        if dp[0]==False:
            return False
        for i in range(1,len(s)):
            for j in range(tmp[i-1]+1,len(t)):
                if s[i]== t[j]:
                    dp[i]=True
                    tmp[i]=j
                    break
            if dp[i]==False:
                return False
        return dp[len(s)-1]
print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))


