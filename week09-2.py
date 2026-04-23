class Solution:
    def reverseList(self, head):        
    #week09-3.py
        if head == None or head.next == None:
            return head
        head2 = head.next
        ans = self. reverseList(head.next)
        head2.next, head.next = head, None
        return ans