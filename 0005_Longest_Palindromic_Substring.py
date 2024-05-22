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
        palabras = []
        contador_inicio = 0
        for a in range(len(s)):
            contador_x =""
            for i in s[contador_inicio:]:
                contador_x = contador_x+i
                palabras.append(contador_x)
            contador_inicio = contador_inicio + 1
            contador_x = "x" * (contador_inicio + 1)

        palindromic_substrings = {}
        for i in palabras:
            if i == i[::-1]:
                palindromic_substrings[len(i)] = i
        characters = palindromic_substrings.keys()
        return(palindromic_substrings[max(characters)])

#Example 1:
string = "babad"
print(Solution().longestPalindrome(string)) #Output: "bab" or "aba"

#Example 2:
string = "cbbd"
print(Solution().longestPalindrome(string)) #Output: bb
