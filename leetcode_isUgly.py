class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        while num%5==0:
            num=num//5
        while num %3 ==0:
            num=num//3
        while num % 2 == 0:
            num = num // 2
        if num ==1:
            return True
        else:
            return False
print(Solution().isUgly(44999))