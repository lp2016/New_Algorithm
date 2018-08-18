#深度优先遍历
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        if root.left:
            if self.hasPathSumHelper(root.left, root.val, sum):
                return True
        if root.right:
            if self.hasPathSumHelper(root.right, root.val, sum):
                return True
        return False

    def hasPathSumHelper(self,root, sumD, sum):
        if root.val == sum and not root.left and not root.right:
            return True
        if root.left:
            if self.hasPathSumHelper(root.left, sumD + root.val, sum):
                return True
        if root.right:
            if self.hasPathSumHelper(root.right, sumD + root.val, sum):
                return True

A=TreeNode(7)
A2=TreeNode(2)
A3=TreeNode(1)

B=TreeNode(11)
B.left=A
B.right=A2


