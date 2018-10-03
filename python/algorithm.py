# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass # function bady cannot be empty!


    """
    Using data structure: dictionary, list
    Using lib func: len(), range()
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # print("Hello World!")
        myDict = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in myDict:
                return [myDict[v], i]
            else:
                myDict[nums[i]] = i
        return []

    """
    using class, modular, floor division, conditional assignment
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(1)
        cur = dummy
        carry = 0
        while (l1 or l2) :
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sumVal = val1 + val2 + carry
            mod = sumVal % 10
            carry = sumVal // 10 # python has divison and floor division
            # print(sumVal, mod, carry)
            cur.next = ListNode(mod)
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry : 
            cur.next = ListNode(1)

        return dummy.next


