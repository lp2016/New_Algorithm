# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        p1=pHead1
        p2 = pHead2
        pHead=None
        if p1.val<=p2.val:
            pHead=pHead1
            p1 = p1.next
        else:
            pHead=pHead2
            p2=p2.next
        p=pHead
        while p1 and p2:
            if p1.val <=p2.val:
                p.next=p1
                p1 = p1.next
            else:
                p.next=p2
                p2 = p2.next
            p=p.next
        if not p1:
            p.next=p2
        else:
            p.next=p1
        return pHead


