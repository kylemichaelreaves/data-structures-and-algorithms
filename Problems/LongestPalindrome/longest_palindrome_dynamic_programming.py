"""
Complexity Analysis

Given n as the length of s,

    Time complexity: O(n2)

    We declare an n * n table dp, which takes O(n2) time.
    We then populate O(n2) states i, j - each state takes O(1) time to compute.

    Space complexity: O(n2)

    The table dp takes O(n2) space.





Algorithm

    Initialize n = s.length and a boolean table dp with size n * n, and all values to false.
    Initialize ans = [0, 0]. This will hold the inclusive bounds of the answer.

    Set all dp[i][i] = true.

    Iterate over all pairs i, i + 1. For each one, if s[i] == s[i + 1], then set dp[i][i + 1] = true and update ans = [i, i + 1].

    Now, we populate the dp table. Iterate over diff from 2 until n. This variable represents the difference j - i.

    In a nested for loop, iterate over i from 0 until n - diff.
        Set j = i + diff.
        Check the condition: if s[i] == s[j] && dp[i + 1][j - 1], we found a palindrome.
        In that case, set dp[i][j] = true and ans = [i, j]

    Retrieve the answer bounds from ans as i, j. Return the substring of s starting at index i and ending with index j.
"""


def longest_palindrome(s: str) -> str:
    """Initialize n = s.length and a boolean table dp with size n * n, and all values to false."""
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    """Initialize ans = [0, 0]. This will hold the inclusive bounds of the answer."""
    ans = [0, 0]

    for i in range(n):
        """Set all dp[i][i] = true."""
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans = [i, i + 1]

    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                ans = [i, j]

    i, j = ans
    return s[i: j + 1]


class Solution:
    pass
