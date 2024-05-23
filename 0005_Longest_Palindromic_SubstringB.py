#Given a string s, return the longest palindromic substring in s.

#Example 1:
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.

#Example 2:
#Input: s = "cbbd"
#Output: "bb"

#Constraints:
#1 <= s.length <= 1000
#s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s

        longest = ""
        for i in range(n):
            # Expandir alrededor del centro para palíndromos de longitud impar
            palindrome1 = expand_around_center(s, i, i)
            # Expandir alrededor del centro para palíndromos de longitud par
            palindrome2 = expand_around_center(s, i, i + 1)

            # Actualizar la cadena más larga encontrada
            longest = max(longest, palindrome1, palindrome2, key=len)

        return longest

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

#Example 1:
string = "babad"
print(Solution().longestPalindrome(string)) #Output: "bab" or "aba"

#Example 2:
string = "cbbd"
print(Solution().longestPalindrome(string)) #Output: bb
