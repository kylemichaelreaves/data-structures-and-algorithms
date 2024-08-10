// Loop through each element x and find if there is another value that equals to target−x.

// Time complexity: O(n2).
// For each element, we try to find its complement by looping through the rest of the array which takes O(n) time.
// Therefore, the time complexity is O(n2).

// Space complexity: O(1).
// The space required does not depend on the size of the input array, so only constant space is used.



class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    return new int[] { i, j };
                }
            }
        }
        // In case there is no solution, we'll just return null
        return null;
    }
}