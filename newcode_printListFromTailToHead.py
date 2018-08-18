# -*- coding:utf-8 -*-
#python 2.7.3
#思路：碰到链表翻转：递归
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return []
        else:
            return self.printListFromTailToHead(listNode.next)+[listNode.val]

