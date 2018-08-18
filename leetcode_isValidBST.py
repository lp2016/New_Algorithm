#思路：中序遍历，单调递增，则为二叉搜索树，否则不是
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root :
            return True
        if not root.left and not root.right:
            return True
        res=[]
        self.isValidBSTHelper(root.left, res)
        res.append(root.val)
        self.isValidBSTHelper(root.right, res)
        for i in  range(0, len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True
    def isValidBSTHelper(self, root, res):
        if not root:
            return
        self.isValidBSTHelper(root.left, res)
        res.append(root.val)
        self.isValidBSTHelper(root.right, res)
