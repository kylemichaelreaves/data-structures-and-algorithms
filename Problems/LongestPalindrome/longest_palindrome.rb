class Solution
  def longest_palindrome(s)
    length_of_string = s.length
    is_palindrome = Array.new(length_of_string) { Array.new(length_of_string, false) }

    start_of_string = 0
    end_of_string = 0

    (length_of_string - 1).downto(0) do |i|
      (i + 1).upto(length_of_string - 1) do |j|
        is_palindrome[i][j] = s[i] == s[j] && (j - i <= 2 || is_palindrome[i + 1][j - 1])
        if is_palindrome[i][j] && (j - i > end_of_string - start_of_string)
          start_of_string = i
          end_of_string = j
        end
      end
    end

    s[start_of_string..end_of_string]
  end
end
