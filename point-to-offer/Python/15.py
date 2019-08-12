# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        firstNode = pHead
        midNode = pHead.next
        firstNode.next = None
        
        while midNode:
            nextNode = midNode.next
            midNode.next = firstNode
            firstNode = midNode
            midNode = nextNode
        
        return firstNode

            
if __name__ == "__main__":
    head = ListNode(0)
    for x in range(1, 5):
        tempNode = ListNode(x)
        tempNode.next = head
        head = tempNode
    
    so = Solution()
    p = so.ReverseList(head)

    while p:
        print(p.val)
        p = p.next
        