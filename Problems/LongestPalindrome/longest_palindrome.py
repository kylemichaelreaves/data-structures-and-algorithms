def longest_palindrome(s: str) -> str:
    length_of_string = len(s)
    is_palindrome = [[False] * length_of_string for _ in range(length_of_string)]

    start_of_string = 0
    end_of_string = 0

    for i in range(length_of_string - 1, -1, -1):
        for j in range(i + 1, length_of_string):
            is_palindrome[i][j] = s[i] == s[j] and (j - i <= 2 or is_palindrome[i + 1][j - 1])
            if is_palindrome[i][j] and (j - i > end_of_string - start_of_string):
                start_of_string = i
                end_of_string = j

    return s[start_of_string:end_of_string + 1]
