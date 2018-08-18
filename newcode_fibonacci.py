# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n==1 or n ==2 :
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)

    def Fibonacci2(self,n):
        if n==0:
            return 0
        if n==1 or n ==2 :
            return 1
        f=[0]
        f.append(1)
        f.append(1)
        for i in range(3,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]

print(Solution().Fibonacci2(39))