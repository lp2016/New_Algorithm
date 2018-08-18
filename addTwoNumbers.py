# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
    def __init__(self,head):
        self.head=ListNode(head)

    def createList(self,data):
        p=self.head
        for i in range(1,len(data)):
            q=ListNode(data[i])
            p.next=q
            p=q

    def printList(self,head):
        p=head
        while p:
            print(p.val," ")
            p=p.next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode(0)
        p=result
        p1=l1
        p2=l2
        flag=0
        while p1 and p2:
            q=ListNode(0)
            p.next=q
            sum=p1.val+p2.val+flag
            if sum <10:
                q.val=sum
                flag=0
            else:
                q.val=sum-10
                flag=1
            p=q
            p1=p1.next
            p2=p2.next
        if p1:
            while p1:
                q = ListNode(0)
                p.next = q
                sum = p1.val +  flag
                if sum < 10:
                    q.val = sum
                    flag = 0
                else:
                    q.val = sum - 10
                    flag = 1
                p = q
                p1 = p1.next
        if p2:
            while p2:
                q = ListNode(0)
                p.next = q
                sum = p2.val +  flag
                if sum < 10:
                    q.val = sum
                    flag = 0
                else:
                    q.val = sum - 10
                    flag = 1
                p = q
                p2 = p2.next
        if flag ==1:
            q = ListNode(1)
            p.next = q
        result=result.next
        return result

data1=[8,9,9,9]
data2=[0]
L1=List(data1[0])
L2=List(data2[0])
L1.createList(data1)
L2.createList(data2)
sum=Solution().addTwoNumbers(L1.head,L2.head)
List(-1).printList(sum)