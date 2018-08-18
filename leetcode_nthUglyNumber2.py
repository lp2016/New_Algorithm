#这一类问题属于寻找第n个符合某一条件的数,看到这种问题会有两种思考方式：
#第一种：从第一个数开始判断，直到找到n个符合条件的数，
#第二种：第k+1个满足条件的数，是不是可以由之前的k个已经确定满足条件的数求出
#第一种复杂度较高
#采用第二种方法实现：每一个新丑数都由已经求出的丑数乘2或乘3或乘5得到，
#刚开始只有一个丑数1，那么由丑数1可以生成三个丑数1*2,1*3,1*5
#新生成的三个丑数2,3,5最小的是2,那么
#利用三个列表t2,t3,t5
#t2记录添加到结果
class Solution:
    def nthUglyNumber(self, n):
        if n==1:
            return n
        t2=[2]
        t3=[3]
        t5=[5]
        for i in range(2,n+1):
            minD=min(t2[0],min(t3[0],t5[0]))
            work=1
            if minD==t2[0]:
                t2.append(t2[0]*2)
                t3.append(t2[0]*3)
                t5.append(t2[0]*5)
                res=t2[0]
                work=0
                del t2[0]
            if minD==t3[0]:
                if work:
                    t2.append(t3[0] * 2)
                    t3.append(t3[0] * 3)
                    t5.append(t3[0] * 5)
                res=t3[0]
                work=0
                del t3[0]
            if minD==t5[0]:
                if work:
                    t2.append(t5[0] * 2)
                    t3.append(t5[0] * 3)
                    t5.append(t5[0] * 5)
                res=t5[0]
                del t5[0]
        return res

Solution().GetUglyNumber_Solution(1)




