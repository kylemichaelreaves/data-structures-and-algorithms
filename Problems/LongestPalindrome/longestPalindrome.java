class Solution {
    public String longestPalindrome(String s) {
        int lengthOfString = s.length();
        var isPalindrome = new boolean[lengthOfString][lengthOfString];

        int start = 0;
        int end = 0;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                isPalindrome[i][j] = s.charAt(i) == s.charAt(j) && (j - 1 <= 2 || isPalindrome[i + 1][j - 1]);
                if (isPalindrome[i][j] && j - i > end - start) {
                    start = i;
                    end = j;
                }
            }
        }
        return s.substring(start, end + 1);
    }
}