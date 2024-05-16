#Given a string s, find the length of the longest substring without repeating characters.

#Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#Example 2:
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.

#Example 3:
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        palabras = []
        contador_inicio = 0
        for a in range(len(s)):
            contador_x =""
            for i in s[contador_inicio:]:
                contador_x = contador_x+i
                palabras.append(contador_x)
            contador_inicio = contador_inicio + 1
            contador_x = "x" * (contador_inicio + 1)
        resultados = []
        for b in palabras:
            caracteres = []
            contador = 0
            for c in b:
                if c not in caracteres:
                    contador = contador+1
                    caracteres.append(c)
                    resultados.append(contador)
                else:
                    break
        return(max(resultados))

#Example 1:
string = "abcabcbb"
print(Solution().lengthOfLongestSubstring(string)) #Output: 3

#Example 2:
string = "bbbbb"
print(Solution().lengthOfLongestSubstring(string)) #Output: 1

#Example 3:
string = "pwwkew"
print(Solution().lengthOfLongestSubstring(string)) #Output: 3
