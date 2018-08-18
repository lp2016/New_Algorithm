
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def ZeroOnePack(self, V, weight, value):
        F = [0] * (V + 1)
        for i in range(0, len(weight)):          #python3超时，将range换成xrange利用python2可以AC
            for v in range(V, weight[i] - 1, -1):
                F[v] = max(F[v], F[v - weight[i]] + value[i])
        return F[V]
    def backPack(self, m, A):
        # write your code here
        return self.ZeroOnePack(m, A, A)
print(Solution().backPack(12,[2, 3, 5, 7]))


