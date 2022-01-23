class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize method to add value and run to next element of list
        :param val: current list's value
        :param next: next element of list
        """
        self.val = val  # initialize value
        self.next = next  # initialize index
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Create merged sorted list linked two lists
        :param list1: the first sorted list
        :param list2: the second sorted list
        :return: merged sorted list
        """
        list3 = ListNode(0, None)  # create list to collect all elements from lists
        head = list3  # head of merged list
        # compare current elements in lists
        while list1 != None and list2 != None:
            # if the second list's element is less it is added to merged list. The second list's index is increased
            if list1.val > list2.val:
                list3.next = ListNode(list2.val)  # adding element
                list2 = list2.next  # moving to next element
                list3 = list3.next  # go to next element of the merged list
            # if the first list's element is less it is added to merged list. The first list's index is increased
            else:
                list3.next = ListNode(list1.val)  # adding element
                list1 = list1.next  # moving to next element
                list3 = list3.next  # go to next element of the merged list
        # when one of two lists is empty move all elements from rest list to the merged list
        if list1 == None:
            while list2 != None:
                list3.next = ListNode(list2.val)  # adding element
                list2 = list2.next  # moving to next element
                list3 = list3.next
        elif list2 == None:
            while list1 != None:
                list3.next = ListNode(list1.val)  # adding element
                list1 = list1.next  # moving to next element
                list3 = list3.next
        return head.next
