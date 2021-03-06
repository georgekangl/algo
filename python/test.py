
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
    # s1 = "abcabcbb"
    # s2 = "bbbbb"
    # s3 = "pwwkew"
    # print(solu.lengthOfLongestSubstring(" "))
    # print(solu.lengthOfLongestSubstring(s1))
    # print(solu.lengthOfLongestSubstring(s2))
    # print(solu.lengthOfLongestSubstring(s3))

    # 5. Longest Palindromic Substring
    # s1 = "babad"
    # s2 = "cbbd"
    # s3 = ""
    # print(solu.longestPalindrome(s1))
    # print(solu.longestPalindrome(s2))
    # print(solu.longestPalindrome(s3))

    # 6. ZigZag Conversion
    # s = "PAYPALISHIRING"
    # numRows = 2
    # print(solu.convert(s, numRows))

    # 7. Reverse Integer
    # print(solu.reverse(123))
    # print(solu.reverse(-123))
    # print(solu.reverse(120))
    # print(solu.reverse(0))
    # print(solu.reverse(2**32))

    # 8. String to Integer (atoi)
    print(solu.myAtoi("123"))
    print(solu.myAtoi("-123"))
    print(solu.myAtoi("            -123"))
    print(solu.myAtoi("         +123"))
    print(solu.myAtoi("  123adafds"))
    print(solu.myAtoi("12adfasdfa3"))
    print(solu.myAtoi("adfasdfa123"))
    print(solu.myAtoi("-adfa123"))
    print(solu.myAtoi("--123"))
    print(solu.myAtoi(""))
    print(solu.myAtoi("   "))
    print(solu.myAtoi("++++"))
    print(solu.myAtoi("12399999999999999999"))
    print(solu.myAtoi("-12999999999999993"))



main()

