#思路：从两边向中间靠拢，每次移动较小的一端
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxd = 0
        n = len(height)
        left = 0
        right = n - 1
        while left != right:
            maxd = max(maxd,(right - left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1


    def maxArea2(self, height):   #暴力法：O(n^2)
        """
        :type height: List[int]
        :rtype: int
        """
        maxd = 0
        maxi = 0
        n = len(height)
        for i in range(0,n-1):
            if height[i] < maxi:
                continue
            else:
                maxi = height[i]
            for j in range(i+1,n):
                maxd = max(maxd,(j-i)*min(height[i],height[j]))
        return maxd