"""
    Time complexity: O(n3)

    The two nested for loops iterate O(n2) times.
    We check one substring of length n, two substrings of length n - 1, three substrings of length n - 2, and so on.

    There are n substrings of length 1, but we don't check them all since any substring of length 1 is a palindrome,
    and we will return immediately.

    Therefore, the number of substrings that we check in the worst case is 1 + 2 + 3 + ... + n - 1.
    This is the partial sum of this series for n - 1, which is equal to 2n⋅(n−1)​=O(n2).

    In each iteration of the while loop, we perform a palindrome check.
    The cost of this check is linear with n as well, giving us a time complexity of O(n3).

    Note that this time complexity is in the worst case and has a significant constant divisor that is dropped by big O.
    Due to the optimizations of checking the longer length substrings first and
    exiting the palindrome check early if we determine that a substring cannot be a palindrome,
    the practical runtime of this algorithm is not too bad.



    Space complexity: O(1)

    We don't count the answer as part of the space complexity.
    Thus, all we use are a few integer variables.

"""



"""

    Create a helper method check(i, j) to determine if a substring is a palindrome.
        To save space, we will not pass the substring itself. 
        Instead, we will pass two indices that represent the substring in question. 
        The first character will be s[i] and the last character will be s[j - 1].
        In this function, declare two pointers left = i and right = j - 1.
        While left < right, do the following steps:
        If s[left] != s[right], return false.
        Otherwise, increment left and decrement right.
        If we get through the while loop, return true.
    Use a for loop to iterate a variable length starting from s.length until 1. 
    This variable represents the length of the substrings we are currently considering.
    Use a for loop to iterate a variable start starting from 0 until and including s.length - length. 
    This variable represents the starting point of the substring we are currently considering.
    In each inner loop iteration, we are considering the substring starting at start until start + length. 
    Pass these values into check to see if this substring is a palindrome. If it is, return the substring.

"""



def longest_palindrome(s: str) -> str:
    """Create a helper method check(i, j) to determine if a substring is a palindrome."""
    """pass two indices that represent the substring"""
    def check(i, j):
        """declare two pointers left = i and right = j - 1."""
        left = i
        right = j - 1
        """While left < right, do the following steps:"""
        while left < right:
            """False if left does not equal right"""
            if s[left] != s[right]:
                return False
            """else, increment left and decrement right"""
            left += 1
            right -= 1

        return True

    """iterate a variable 'length' starting from s.length until 1"""
    """representing the length of the substrings we are currently considering"""
    for length in range(len(s), 0, -1):
        """iterate a variable 'start' starting from 0 until and including s.length - length"""
        """representing the starting point of the substring we are currently considering."""
        for start in range(len(s) - length + 1):
            """if it's a palindrome…"""
            if check(start, start + length):
                """return it by slicing its string by start through start + length"""
                return s[start: start + length]

    return ""


class Solution:
    pass
