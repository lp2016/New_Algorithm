#深度优先遍历
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        if not root:
            return []
        if root.val == sum and not root.left and not root.right:
            return [[root.val]]
        if root.left:
            self.pathSumHelper(root.left, root.val, sum, [root.val], res)
        if root.right:
            self.pathSumHelper(root.right, root.val, sum, [root.val], res)
        return res

    def pathSumHelper(self,root, sumD, sum, r, res):
        if root.val +sumD == sum and not root.left and not root.right:
            t = r[:]
            t.append(root.val)
            res.append(t)
            return
        if root.left:
            t=r[:]
            t.append(root.val)
            self.pathSumHelper(root.left, sumD + root.val, sum, t[:], res)
        if root.right:
            t = r[:]
            t.append(root.val)
            self.pathSumHelper(root.right, sumD + root.val, sum, t[:], res)



