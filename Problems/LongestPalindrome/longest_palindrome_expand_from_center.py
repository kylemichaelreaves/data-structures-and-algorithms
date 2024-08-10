"""
Algorithm

    Create a helper method expand(i, j) to find the length of the longest palindrome centered at i, j.
        Set left = i and right = j.
        While left and right are both in bounds and s[left] == s[right], move the pointers away from each other.
        The formula for the length of a substring starting at left and ending at right is right - left + 1.
        However, when the while loop ends, it implies s[left] != s[right]. Therefore, we need to subtract 2. Return right - left - 1.
    Initialize ans = [0, 0]. This will hold the inclusive bounds of the answer.
    Iterate i over all indices of s.
        Find the length of the longest odd-length palindrome centered at i: oddLength = expand(i, i).
        If oddLength is the greatest length we have seen so far, i.e. oddLength > ans[1] - ans[0] + 1, update ans.
        Find the length of the longest odd-length palindrome centered at i: evenLength = expand(i, i + 1).
        If evenLength is the greatest length we have seen so far, update ans.
    Retrieve the answer bounds from ans as i, j. Return the substring of s starting at index i and ending with index j.

Complexity Analysis



Given n as the length of s,

    Time complexity: O(n2)
    There are 2n−1=O(n) centers. For each center, we call expand, which costs up to O(n).
    Although the time complexity is the same as in the DP approach, the average/practical runtime of the algorithm is much faster.
    This is because most centers will not produce long palindromes, so most of the O(n) calls to expand will cost far less than n iterations.

    The worst case scenario is when every character in the string is the same.

    Space complexity: O(1)

    We don't use any extra space other than a few integers.
    This is a big improvement on the DP approach.

"""


def longest_palindrome(s: str) -> str:
    def expand(i, j):
        left = i
        right = j

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

    ans = [0, 0]

    for i in range(len(s)):
        odd_length = expand(i, i)
        if odd_length > ans[1] - ans[0] + 1:
            dist = odd_length // 2
            ans = [i - dist, i + dist]

        even_length = expand(i, i + 1)
        if even_length > ans[1] - ans[0] + 1:
            dist = (even_length // 2) - 1
            ans = [i - dist, i + 1 + dist]

    i, j = ans
    return s[i: j + 1]


class Solution:
    pass
