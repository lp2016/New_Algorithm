class Solution:

    def create_next(self, next, S, T, m):
        for j in range(2, m):
            res = 0
            for k in range(1, j):
                if T[0:k] == T[j-k:j]:
                    res = max(res, k)
            next.append(res)
    def create_next2(self, next, S, T, m):
        k = -1
        j = 0
        while j < len(T) - 1:
            if k == -1 or T[k] == T[j]:
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]

    def pattern_matching(self, S, T):
        i = 0
        j = 0
        n = len(S)
        m = len(T)
        next = [-1]*len(T)
        self.create_next2(next, S, T, m)
        print(next)
        while i < n and j < m:
            if S[i] == T[j]:
                i = i + 1
                j = j + 1
            else:
                j = next[j]
        if j == m:
            return i - j             #如果能在主串中找到匹配的字串，返回匹配的开始位置
        else:
            return -1                #如果找不到匹配的字串，返回-1
print(Solution().pattern_matching("ababaababcb","ababc"))