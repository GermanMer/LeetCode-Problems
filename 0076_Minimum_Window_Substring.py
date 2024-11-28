# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

# Follow up: Could you find an algorithm that runs in O(m + n) time?

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dict_t = Counter(t)  # Contar caracteres en t
        required = len(dict_t)  # Número de caracteres únicos en t que deben estar en la ventana

        # Inicializar punteros y contadores
        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)

        # Resultados
        min_len = float('inf')
        min_left, min_right = 0, 0

        while r < len(s):
            char = s[r]
            window_counts[char] += 1

            # Verificar si el carácter actual cumple con la cantidad requerida
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Intentar contraer la ventana hasta que ya no sea válida
            while l <= r and formed == required:
                char = s[l]

                # Actualizar el resultado si la ventana actual es más pequeña
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_left, min_right = l, r + 1

                # Reducir el conteo del carácter que se está moviendo fuera de la ventana
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                l += 1  # Mover el límite izquierdo de la ventana

            r += 1  # Mover el límite derecho de la ventana

        return s[min_left:min_right] if min_len != float('inf') else ""

# Example 1:
s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"
print(Solution().minWindow(s, t))

# Example 2:
s = "a"
t = "a"
# Output: "a"
print(Solution().minWindow(s, t))

# Example 3:
s = "a"
t = "aa"
# Output: ""
print(Solution().minWindow(s, t))
