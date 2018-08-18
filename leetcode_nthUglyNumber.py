class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=1
        number=2
        d={1}
        d2=set()
        while True:
            work = 0
            if c==n:
                return number-1
            num=number
            while num%5 ==0:
                num=num//5
                if num in d:
                    d.add(number)
                    c+=1
                    number += 1
                    work=1
                    break
                if num in d2:
                    d2.add(number)
                    number += 1
                    work = 1
                    break
            if work:
                continue
            while num % 3 == 0:
                num = num // 3
                if num in d:
                    d.add(number)
                    c+=1
                    number += 1
                    work=1
                    break
                if num in d2:
                    d2.add(number)
                    number += 1
                    work = 1
                    break
            if work:
                continue
            while num % 2 == 0:
                num = num // 2
                if num in d:
                    d.add(number)
                    c+=1
                    number += 1
                    work=1
                    break
                if num in d2:
                    d2.add(number)
                    number += 1
                    work = 1
                    break
            if work:
                continue
            d2.add(number)
            number+=1



print(Solution().nthUglyNumber(6))


