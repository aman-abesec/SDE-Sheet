#======================================================
#      21. Merge Two Sorted Lists
#      https://leetcode.com/problems/merge-two-sorted-lists/
#
#=========================================================
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:return list2
        if list2==None:return list1
        head=tail=None
        ptr1,ptr2=list1,list2
        if ptr1.val>=ptr2.val:
            tail=head=ptr2
            ptr2=ptr2.next
        else:
            tail=head=ptr1
            ptr1=ptr1.next
        while ptr1!=None and ptr2!=None:
            if ptr1.val<=ptr2.val:
                tail.next=ptr1
                tail=ptr1
                ptr1=ptr1.next
            else:
                tail.next=ptr2
                tail=ptr2
                ptr2=ptr2.next
        if ptr1==None:
            tail.next=ptr2
        else:
            tail.next=ptr1
        return head


#============================
#        Method2
#============================
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp = ans
        temp1,temp2=list1,list2
        while temp1!=None and temp2!=None:
            if temp1.val<=temp2.val:
                temp.next=temp1
                temp=temp1
                temp1=temp1.next
            else:
                temp.next=temp2
                temp=temp2
                temp2=temp2.next
        if temp1==None:temp.next=temp2
        else:temp.next=temp1
        return ans.next
