def longest_palindrome(s)
  "helper method to check if a string is a palindrome"

  def check(i, j)
    "left and right pointers"
    left = i
    right = j - 1

    "so long as the left index is less than the right "
    while left < right
      "false if the strings don't match"
      return false if s[left] != s[right]
      "increment left and decrement right"
      left += 1
      right -= 1
    end
  end

  "Iterate a variable 'i' from s.length down to 0, representing the length of the substrings being considered."
  (s.length).downto(0).each do |i|
    "Iterate a variable 'j' from 0 to s.length - i, representing the starting point of the current substring."
    (0..(s.length - i)).each do |j|
      "If the substring is a palindrome, return it by slicing its indices."
      return s[j, i] if check(j, i)
    end
  end
end
