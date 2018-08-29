#f[i]表示以第i个元素结尾的不包含重复元素的字串的最大长度
def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)
    times = [-1]*26
    f = [1]*len(s)
    times[ord(s[0])-97] = 0
    res = 0
    for i in range(1,len(s)):
        if times[ord(s[i])-97] == -1:
            f[i] = f[i-1] + 1
        else:
            d = i - times[ord(s[i])-97]
            if d > f[i-1]:
                f[i] = f[i - 1] + 1
            else:
                f[i] = d
        times[ord(s[i]) - 97] = i
        res = max(res,f[i])
    return res



#查找字符串S中不含有重复字符的最长子串的长度
def lengthOfLongestSubstring_2(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    l = {}
    right = 0
    left = 0
    while right < len(s):
        if s[right] not in l:
            l[s[right]] = 1
            right += 1
            result = max(result, len(l))
        else:
            del l[s[left]]   #注意删除list中的元素时间复杂度为O（N）
            left += 1
    return result


print(lengthOfLongestSubstring("abcabcbb"))