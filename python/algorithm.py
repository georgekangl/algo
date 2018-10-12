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

    """
    using set
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mySet = set() #set, set() to create an empty set, {} to create an empty dict
        left, right, res = 0, 0, 0 # not like left = 0, right = 0, res = 0
        while right < len(s):
            if s[right] not in mySet:
                mySet.add(s[right])
                right += 1
            else:
                res = max(res, right - left)
                mySet.remove(s[left])
                left += 1

        res = max(res, right - left)
        return res

    def getPalindromeOdd(self, s, center):
        left = center - 1
        right = center + 1
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        # print(type(left), type(right))
        return s[left + 1 : right] # using [:] to get substring, not [,]

    def getPalindromeEven(self, s, center):
        left = center
        right = center + 1
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1 : right]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        res = ""
        for i in range(len(s)):
            oddPalin = self.getPalindromeOdd(s, i) # call member function as an instance
            evenPalin = self.getPalindromeEven(s, i)
            # print(oddPalin, evenPalin)
        
            if len(oddPalin) >= len(evenPalin):
                if len(oddPalin) >= maxLen:
                    maxLen = len(oddPalin)
                    res = oddPalin 
            else:
                if len(evenPalin) >= maxLen:
                    maxLen = len(evenPalin)
                    res = evenPalin

        return res

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows <= 1):
            return s
        # chars = [[]] * numRows # this puts the same list in all numRows places
        chars = [[] for _ in range(numRows)]
        charIndex = -1
        increase = 1
        res = ""
        for i in range(len(s)):
            # print(chars)
            charIndex += increase
            # print(charIndex, chars[charIndex])
            chars[charIndex].append(s[i])
            # print(charIndex, chars[charIndex])
            if charIndex == 0:
                increase = 1
            if charIndex == numRows - 1:
                increase = -1
        
        for l in chars:
            for c in l:
                res += c

        return res

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        x = abs(x)
        nums = []
        while x > 0 :
            nums.append(x % 10)
            x = x // 10

        res = 0
        for n in nums: 
            res = res * 10 + n
            
        res = res * sign
        if (res > 2**31 - 1 or res < -2**31):
            return 0

        return res

    def preProcess(sefl, str):
        if str == "":
            return ""
        i = 0
        res = ""
        while (i < len(str) and str[i] == ' '):
            i += 1
        if i >= len(str):
            return res
        if str[i] == '-' or str[i] == '+':
            res += str[i]
            i += 1
        while i < len(str) and str[i].isdigit():
            res += str[i]
            i += 1
        return res


    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = self.preProcess(str)
        # print("!!!    " + str)
        if str == "":
            return 0
        sign = -1 if str[0] == '-' else 1
        # i = 0
        if str[0] == '-' or str[0] == '+':
            str = str[1:]
        if str == "":
            return 0
        # res = 0
        # for i in range(len(str)):
        #     res = res * 10 + ord(str[i])
        #     i += 1
        # res = res * sign

        res = int(str) * sign
        if res > 2**31 - 1:
            return 2**31 - 1
        if res < -2**31:
            return -2**31

        return res

                



        

