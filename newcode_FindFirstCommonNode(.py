# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        d1 = {}
        d2 = {}
        p1 = pHead1
        p2 = pHead2
        while p1 and p2:
            if p1 in d2:
                return p1
            d1[p1] = 1
            if p2 in d1:
                return p2
            d2[p2] = 1
            p1 = p1.next
            p2 = p2.next
        while p1:
            if p1 in d2:
                return p1
            p1 = p1.next
        while p2:
            if p2 in d1:
                return p2
            p2 = p2.next
        return None


