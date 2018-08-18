#思路：深度优先搜索
##如果可以 以第i个人作为源开始搜索，说明这之前搜索的人都不认识i，那么也就说明i在一个单独的朋友圈
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m  = len(M)
        visit = [False]*m
        count =0
        for i in range(0, m):
            if not visit[i]:
                self.findCircleNumHelper(i, visit, M)
                count += 1
        return count

    def findCircleNumHelper(self, tmp, visit, M):
        visit[tmp] = True
        for i in range(0, len(M)):
            if M[tmp][i] and not visit[i]:
                self.findCircleNumHelper(i, visit, M)


print(Solution().findCircleNum([[1]]))