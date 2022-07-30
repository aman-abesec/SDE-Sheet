#======================================================
#      234. Palindrome Linked List
#      https://leetcode.com/problems/palindrome-linked-list/
#      https://youtu.be/-DtNInqFUXs
#=========================================================
#T-O(n)+O(n)
#S-O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        curr=head
        while curr!=None:
            stack.append(curr.val)
            curr=curr.next
        while head!=None:
            if stack[-1]!=head.val:
                return False
            head=head.next
            stack.pop()
        return True

class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        return prev


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        slow.next=self.reverse(slow.next)
        slow=slow.next
        temp=head
        while slow!=None:
            if slow.val!=temp.val:
                return False
            slow=slow.next
            temp=temp.next
        return True
