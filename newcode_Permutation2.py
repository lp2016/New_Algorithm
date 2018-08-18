# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        res = []
        L = len(ss)

        self.PermutationHelper(0, L, [], res, ss)

    def PermutationHelper(self, j, L, path, res, ss):
        if j == L :
            return

        for i in range(j+1,L):
            path.append(ss[i])
            if i == L - 1:
                res.append(path)
            self.swap(ss,i,j)
            self.PermutationHelper(i + 1, L, path, res, ss)
            self.swap(ss,i,j)

    def swap(self):
        pass


