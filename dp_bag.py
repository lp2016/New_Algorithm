class Solution:
    def bag(self, weight, value,W):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        F=[0]*(W+1)
        G=[[0 for j in range(W+1)]for i in range(len(weight)+1)]
        test=999
        for i in range(0, len(weight)):
            for v in range(W, weight[i] - 1, -1):
                if F[v]<F[v-weight[i]]+value[i]:
                    F[v] =F[v - weight[i]] + value[i]
                    G[i][v]=1
                test = F[v]

            print()

        # i=len(weight)-1
        # v=W
        # while i>=0:
        #     if F[v]==F[v-weight[i]]+value[i]:
        #         print("选取",i)
        #     else:
        #         print("未选取",i)
        #         v=v-weight[i]
        #     i=i-1
        print(F)
Solution().bag([2,2,6,5,4],[6,3,5,4,6],10)
