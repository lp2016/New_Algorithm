# -*- coding:utf-8 -*-
class Solution:
    #最笨方法：查找最小值
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray)==0 :
            return 0
        minNumber=rotateArray[0]
        for item in rotateArray:
            minNumber=min(minNumber,item)
        return minNumber
    #稍微改进
    def minNumberInRotateArray1(self, rotateArray):
        if len(rotateArray)==0 :
            return 0
        for i in range(0,len(rotateArray)-1):
            if rotateArray[i]>rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]

    #递归解法
    def minNumberInRotateArray2(self, rotateArray):
        l=len(rotateArray)
        if l==0 :
            return 0
        if l == 1:
            return rotateArray[0]
        if l== 2:
            return min(rotateArray[0],rotateArray[1])
        if rotateArray[0]<rotateArray[l-1]:
            return rotateArray[0]
        if l%2!=0:
            if rotateArray[l//2] <rotateArray[l//2-1] and rotateArray[l//2] <rotateArray[l//2+1]:
                return rotateArray[l//2]
            elif rotateArray[0]>rotateArray[l//2-1]:
                return self.minNumberInRotateArray2(rotateArray[0:l // 2])
            else:
                return self.minNumberInRotateArray2(rotateArray[l // 2+1:])
        else:
            if rotateArray[0]>rotateArray[l//2-1]:
                return self.minNumberInRotateArray2(rotateArray[0:l // 2])
            else:
                return self.minNumberInRotateArray2(rotateArray[l // 2 :])

    #二分方法
    def minNumberInRotateArray3(self, rotateArray):
        l=len(rotateArray)
        if l == 0:
            return 0
        if rotateArray[0]<rotateArray[l-1]:
            return rotateArray[0]
        low=0
        high=l-1
        while low< high:
            mid=(low+high)//2
            if rotateArray[low]==rotateArray[mid] and rotateArray[mid] == rotateArray[high]:
                return min(rotateArray[low:high+1])
            if low == mid:
                return min(rotateArray[low],rotateArray[low+1])
            if rotateArray[low]<=rotateArray[mid]:
                low=mid
            elif rotateArray[low]>rotateArray[mid]:
                high=mid

print(Solution().minNumberInRotateArray3([0,1,1,1,1]))

