class Solution:
    #思路：假设x个1，y个2,那么满足x+2y=number
    #若number是奇数，则x是奇数，x取1,3,5,...，number；若number是偶数，则x是偶数，x取0,2,4,...,number
    #y=(number-x)//2
    #对于每一个x，y：就是排列组合的问题了：x+y个空，选择x个1,即C(x+y,x)
    #另一种解法就是斐波那些数列：青蛙跳1级台阶有1种跳法，2级台阶有2种跳法
    # 3级台阶时可以从1级台阶跳上来也可以从2级台阶跳上来，即等于1级台阶的跳法加2级台阶的跳法
    # 因此n级台阶共有n-2级台阶跳法数+n-1级台阶跳法数
    def jumpFloor(self, number):
        if number%2==0:
            x=0
        else:
            x=1
        c=0
        while x<=number:
            y=(number-x)//2
            c=c+self.jiecheng(x+y)//(self.jiecheng(x)*self.jiecheng(y))
            x+=2
        return c
    def jiecheng(self,n):
        if n==0:
            return 1
        number=1
        for i in range(1,n+1):
            number=number*i
        return number

print(Solution().jumpFloor(5))



