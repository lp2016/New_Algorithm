#思路：序列最后一个为根节点，除去最后一个数的序列，左侧部分全部小于根节点，右侧部分全部大于根节点
#一次递归判断左\右侧部分是否为某一二叉搜索树的后序遍历
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        left = []
        right = []
        i = 0
        while i < len(sequence)-1:
            if sequence[i] < root:
                left.append(sequence[i])
            else:
                break
            i+=1
        while i < len(sequence)-1:
            if sequence[i] > root:
                right.append(sequence[i])
            else:
                return False
            i+=1
        if len(left) > 0:
            if not self.VerifySquenceOfBST(left):
                return False
        if len(right) > 0:
            if not self.VerifySquenceOfBST(right):
                return False

        return True

    def VerifySquenceOfBSTHelper(self, sequence):
        root = sequence[-1]
        left = []
        right = []
        i = 0
        j = 0
        while i < len(sequence):
            if sequence[i] < root:
                left.append(sequence[i])
            else:
                break
            i += 1
        while i < len(sequence):
            if sequence[i] > root:
                right.append(sequence[i])
            else:
                return False
            i += 1
        if len(left) > 0:
            if not self.VerifySquenceOfBST(left):
                return False
        if len(right) > 0:
            if not self.VerifySquenceOfBST(right):
                return False
        return True


print(Solution().VerifySquenceOfBST([7,4,6,5]))