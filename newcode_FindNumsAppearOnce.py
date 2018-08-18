# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) <= 1:
            return []
        tmp = 0
        for i in range(0,len(array)):
            tmp =tmp ^ array[i]
        index = self.FindFirstBit(tmp)  #从右到左第一个不为0的位置
        tmp1 = 0
        tmp2 = 0
        for i in range(0,len(array)):
            if self.Is0(array[i], index):
                tmp1 = tmp1 ^ array[i]
            else:
                tmp2 = tmp2 ^ array[i]
        return [tmp1,tmp2]

    #查找某一个数字的二进制形式的最低位第一个为1的位
    def FindFirstBit(self, number):
        i = 0
        while True:
            if number & 1 == 1:
                return i
            number = number >> 1
            i += 1

    def Is0(self, number, index):    #利用右移运算符判断右边数第index位是否为1
        return (number >> index) & 1





    def FindNumsAppearOnce2(self, array):              #利用字典
        # write code here
        if len(array) <= 1:
            return []
        d = {}
        for i in range(0, len(array)):
            if array[i] in d:
                d[array[i]] += 1
            else:
                d[array[i]] = 1
        res = []
        for key, val in d.items():
            if val == 1:
                res.append(key)
                if len(res) == 2:
                    return res


print(Solution().FindNumsAppearOnce([1,5,2,5,4,1,7,7]))