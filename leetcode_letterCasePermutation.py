class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L=len(S)
        res=[]
        path=[]
        self.letterCasePermutationHelper(S,0,path,L,res)
        return res

    def letterCasePermutationHelper(self,S,i,path,L,res):
        if i ==L:
            res.append(''.join(path))
            return
        if S[i].upper()!=S[i].lower():
            path.append(S[i].lower())
            self.letterCasePermutationHelper(S,i+1,path,L,res)
            del path[-1]
            path.append(S[i].upper())
            self.letterCasePermutationHelper(S,i+1,path,L,res)
            del path[-1]
        else:
            path.append(S[i])
            self.letterCasePermutationHelper(S, i + 1, path, L, res)
            del path[-1]


Solution().letterCasePermutation("a1b2")