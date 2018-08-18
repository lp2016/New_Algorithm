#功能：寻找字符串中的最长重复字串
#思路：利用后缀数组实现
#后缀数组中包含以每一个字符开头的字串，所以如果有重复字串，那么该子串肯定会出现在后缀数组中的某两个元素的前缀上
#之所以对后缀数组进行排序是因为：如果不排序，需要两两比较数组中的元素（O（n^2）），而每个元素的长度最大为n，
# 因此如果不排序，两两比较需要O（n^3）
#如果排序的话，按照ascil排序后的后缀数组，重复元素最多的肯定是相邻两个，因此只需要比较后缀数组中相邻两个元素即可，
# 即post[i]与psot[i+1]，时间复杂度为O（n^2）
def longestRepeatStr(s):
    post = []
    for i in range(len(s)-1, -1, -1):
        post.append(s[i:])
    post.sort()   #此处时间复杂度为O(n*n*log n) ,n*log n 是排序算法的复杂度，最前面的n表示每一个元素长度为n
    maxD = 0
    for i in range(0, len(post)-1):
        j = 0
        while j < len(post[i]) and j < len(post[i+1]):
            if post[i][0:j+1] !=post[i+1][0:j+1]:
                break
            else:
                maxD = max(maxD, j+1)
            j = j + 1
    return maxD


print(longestRepeatStr("thisisastringwhichisis"))

