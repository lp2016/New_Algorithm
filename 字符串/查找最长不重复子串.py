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
            del l[s[left]]
            left += 1
    return result