#思路：动态规划
#没有额外空间使用啊，题目为啥说O(N)的额外空间可以加分。。。
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m=len(triangle)
        for i in range(1,m):
            triangle[i][0]+=triangle[i-1][0]
            for j in range(1,len(triangle[i])-1):
                triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
            triangle[i][len(triangle[i])-1]+=triangle[i-1][len(triangle[i-1])-1]
        return min(triangle[m-1])
print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))