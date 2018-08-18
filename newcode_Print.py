# -*- coding:utf-8 -*-
#利用两个栈：一个栈tmp1存储奇数层元素，另一个栈tmp2存储偶数层元素
#如果栈为空，说明当前层遍历完成，level需要加1
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        tmp1 = []
        tmp2 = [pRoot]
        tmp = []
        level = 0
        while len(tmp2) > 0 or len(tmp1) > 0:
            if level % 2 == 0:
                t = tmp2.pop()
                tmp.append(t.val)
                if len(tmp2) == 0:
                    level += 1
                    res.append(tmp[:])
                    tmp = []
                if  t.left:
                    tmp1.append(t.left)
                if t.right:
                    tmp1.append(t.right)
            else:
                t = tmp1.pop()
                tmp.append(t.val)
                if len(tmp1) == 0:
                    level += 1
                    res.append(tmp[:])
                    tmp = []

                if  t.right:
                    tmp2.append(t.right)
                if t.left:
                    tmp2.append(t.left)

        return res

a5 = TreeNode(5)
a7 = TreeNode(7)
a9 = TreeNode(9)
a11 = TreeNode(11)

a6 = TreeNode(6)
a8= TreeNode(8)
a10 = TreeNode(10)

a6.left = a5
a6.right = a7

a10.left = a9
a10.right = a11

a8.left = a6
a8.right = a10

print(Solution().Print(a8))