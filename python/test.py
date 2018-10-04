
from algorithm import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkList(myArray):
    dummy = ListNode(1)
    cur = dummy
    for n in myArray:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def printLinkList(l):
    print("LinkList as below:")
    while (l != None):
        print(l.val, end='')
        print(' ', end='')
        l = l.next

def main():
    solu = Solution()

    # # two sum test case
    # nums = [1,2,3,4,5]
    # target = 7
    # res = solu.twoSum(nums, target)
    # print(res)

    # add two number test case
    # l1 = createLinkList([1,2,3])
    # l2 = createLinkList([5,6,7,8])
    # res = solu.addTwoNumbers(l1, l2)
    # printLinkList(res)

    # longest substring without repeating characters
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    print(solu.lengthOfLongestSubstring(" "))
    print(solu.lengthOfLongestSubstring(s1))
    print(solu.lengthOfLongestSubstring(s2))
    print(solu.lengthOfLongestSubstring(s3))


main()

