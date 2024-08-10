"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

"""two sum brute force"""
"""Loop through each element x and find if there is another value that equals to target−x."""
"""
    Time complexity: O(n2).
    For each element, we try to find its complement by looping through the rest of the array which takes O(n) time. 
    Therefore, the time complexity is O(n2).

    Space complexity: O(1).
    The space required does not depend on the size of the input array, so only constant space is used.
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return None
