#Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#'?' Matches any single character.
#'*' Matches any sequence of characters (including the empty sequence).
#The matching should cover the entire input string (not partial).

#Example 1:
#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".

#Example 2:
#Input: s = "aa", p = "*"
#Output: true
#Explanation: '*' matches any sequence.

#Example 3:
#Input: s = "cb", p = "?a"
#Output: false
#Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

#Constraints:
#0 <= s.length, p.length <= 2000
#s contains only lowercase English letters.
#p contains only lowercase English letters, '?' or '*'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Longitudes de la cadena y del patrón
        m, n = len(s), len(p)

        # Tabla dp donde dp[i][j] es True si s[:i] coincide con p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # La coincidencia de una cadena vacía con un patrón vacío es verdadera
        dp[0][0] = True

        # Inicializar la primera fila para patrones que comienzan con '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Llenar la tabla dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' puede coincidir con ninguna o con uno o más caracteres
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    # Coincidencia de un solo carácter o '?'
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '?')

        # La última celda de la tabla indica si toda la cadena coincide con todo el patrón
        return dp[m][n]

#Example 1:
s = "aa"
p = "a"
print(Solution().isMatch(s, p))
#Output: false

#Example 2:
s = "aa"
p = "*"
#Output: true
print(Solution().isMatch(s, p))

#Example 3:
s = "cb"
p = "?a"
#Output: false
print(Solution().isMatch(s, p))
