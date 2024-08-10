"""
Use two iterations.
In the first iteration, add each element's value as a key and its index as a value to the hash table.
In the second iteration, check if each element's complement (target−nums[i]) exists in the hash table.
If it does exist, we return current element's index and its complement's index.
Beware that the complement must not be nums[i] itself!

Time complexity: O(n).
We traverse the list containing n elements exactly twice.
Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n).

Space complexity: O(n).
The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.

"""


class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[]{i, map.get(complement)};
            }
        }
        // In case there is no solution, we'll just return null
        return null;
    }
}