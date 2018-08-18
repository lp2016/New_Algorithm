# -*- coding:utf-8 -*-
#思路：递归的思想
# HasSubtree（）函数用来找到root1的某一个结点v使得 v的值和root2的根节点的值相等，即v.val=root2.val
# HasSubtree2（）函数用来判断root1的每一个孩子结点是否和root2的对应结点相同。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2 or not pRoot1:
            return False
        if pRoot1.val == pRoot2.val:
            if self.HasSubtree2(pRoot1,pRoot2):
                return True
            elif pRoot1.left:
                if self.HasSubtree(pRoot1.left, pRoot2):
                    return True
            elif pRoot1.right:
                if self.HasSubtree(pRoot1.right,pRoot2):
                    return True
            else:
                return False
        else:
            if pRoot1.left:
                if self.HasSubtree(pRoot1.left, pRoot2):
                    return True
            elif pRoot1.right:
                if self.HasSubtree(pRoot1.right,pRoot2):
                    return True
            else:
                return False

    def HasSubtree2(self,pRoot1,pRoot2):

        if pRoot1.val != pRoot2.val:
            return False
        if pRoot1.left and pRoot2.left:
            if not self.HasSubtree2(pRoot1.left, pRoot2.left):
                return False
        if pRoot1.right and pRoot2.right:
            if not self.HasSubtree2(pRoot1.right, pRoot2.right):
                return False
        if (not pRoot1.left and pRoot2.left) or (not pRoot1.right and pRoot2.right):
            return False
        return True



