# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:

    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        head=RandomListNode(pHead.label)
        p=pHead
        q=head
        d={}
        while p:
            if p.next:
                tmp=RandomListNode(p.next.label)
                q.next=tmp
                d[p.next]=tmp
            p=p.next
            q=q.next

        p = pHead
        q = head
        while p:
            if p.random:
                q.random = d[p.random]
            p = p.next
            q = q.next

        return head



