# -*- coding:utf-8 -*-
#思路：正数的话，就按照除2取余的方法统计1的个数
#负数：求绝对值对应的二进制，然后扩展成32位的二进制，然后求补码，再求补码加1中1的个数
class Solution:
    def NumberOf1(self, n):
        if n==0:
            return 0
        if n>0:
           return self.count(n)
        else:
            n=abs(n)
            x=[]
            while n > 1:
                if n % 2:
                    x.append(1)
                else:
                    x.append(0)
                n = n // 2
            x.append(1)
            k=32-len(x)
            y=(k*[0])
            x.extend(y)
            c=0
            tmp=list(map(lambda x: (x + 1) % 2, x))
            for i in range(0,32):
                c+=tmp[i]*(2**i)
            return self.count(c+1)
    def count(self,n):
        po = 1
        na = 1
        while n > 1:
            if n % 2:
                po = po + 1
            else:
                na += 1
            n = n // 2
        return po






print(Solution().NumberOf1(-1))

