from typing import List


"""a hash table is the best way to maintain a mapping of each element in the array to its index"""
"""a hash table supports fast lookup in near constant time."""
""" 'near' because if a collision occurred, a lookup could degenerate to O(n) time. """


""""
    Time complexity: O(n).
    We traverse the list containing n elements exactly twice. 
    Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n).

    Space complexity: O(n).
    The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]



