# -*- coding:utf-8 -*-
from 链表.LinkList import create_LinkList,print_LinkList
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        head = ListNode(0)
        head.next = pHead
        later  = head
        before = pHead
        while before.next:
            if later.next.val == before.next.val:
                before = before.next
                while before.next and later.next.val == before.next.val:
                    before = before.next
                before = before.next
                later.next = before
                if not before:
                    break

            else:
                later = later.next
                before = before.next
        return head.next
    def deleteDuplication2(self, pHead):
        # write code here
        if not pHead:
            return None
        head = ListNode(0)
        head.next = pHead
        later  = head
        before = pHead
        while before.next:
            if later.next.val == before.next.val:
                before = before.next
                while before.next and later.next.val == before.next.val:
                    before = before.next
                before = before.next
                later.next = before
                if not before:
                    break

            else:
                later = later.next
                before = before.next
        return head.next


if __name__ == "__main__":

    head = create_LinkList([1,2,3,3,4,4,5])
    print_LinkList(Solution().deleteDuplication(head))

