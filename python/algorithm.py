
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution:
    def __init__(self):
        pass # function bady cannot be empty!

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




