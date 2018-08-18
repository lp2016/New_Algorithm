# -*- coding:utf-8 -*-
#思路：利用字典，以字符为key，字符的个数为value，遍历一遍求得每个字符出现的次数
#再遍历一遍字符串s，找到第一个只出现一次的字符
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        d={}
        for i in range(0,len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i  in range(0,len(s)):
            if d[s[i]] ==1:
                return i


print(Solution().FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp"))

