# _*_ coding=utf-8 _*_


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):

    def two_sum(self, nums, target):
        """
        直接循环查找
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return sorted([i, j])

    def two_sum_binary(self, nums, target):
        """
        想记住元素位置，然后排序，最后使用二分查找
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[0])

        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i + 1, len(new_nums) - 1, b)
            else:
                j = self.binary_search(new_nums, 0, i - 1, b)
            if j:
                break
        return sorted([new_nums[i][1], new_nums[j][1]])

    def binary_search(self, nums, left, right, val):
        while left <= right:
            mid = (left + right) // 2
            if val == nums[mid][0]:
                return mid
            elif val < nums[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return
