# We can scramble a string s to get a string t using the following algorithm:
    # 1) If the length of the string is 1, stop.
    # 2) If the length of the string is > 1, do the following:
        # Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
        # Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
        # Apply step 1 recursively on each of the two substrings x and y.
    # Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

# Example 1:
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
    # "great" --> "gr/eat" // divide at random index.
    # "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
   # "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
    # "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
    # "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
    # "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
    # The algorithm stops now, and the result string is "rgeat" which is s2.
    # As one possible scenario led s1 to be scrambled to s2, we return true.

# Example 2:
# Input: s1 = "abcde", s2 = "caebd"
# Output: false

# Example 3:
# Input: s1 = "a", s2 = "a"
# Output: true

# Constraints:
# s1.length == s2.length
# 1 <= s1.length <= 30
# s1 and s2 consist of lowercase English letters.

# La solución anterior no es adecuada para resolver correctamente el problema de "Scramble String", aunque tiene una base válida en cuanto a la verificación de la igualdad de caracteres. Sin embargo, este enfoque solo verifica si las cadenas tienen los mismos caracteres (es decir, si son anagramas), lo cual no es suficiente para determinar si una cadena es un "scramble" de la otra.
# Ejemplo:
# s1 = "abcde"
# s2 = "caebd"
# Estas dos cadenas tienen los mismos caracteres, por lo que sorted(s1) == sorted(s2) sería True. Sin embargo, no pueden ser "scrambles" una de la otra. La solución correcta debe ser capaz de detectar que no es posible reorganizar las subcadenas de s1 para formar s2 siguiendo las reglas del algoritmo.

# Lo que realmente necesitamos es una recursión con memoización para verificar si se pueden dividir las cadenas en subcadenas, intercambiar algunas de ellas y hacer que coincidan. Esto implica dividir las cadenas en subcadenas de manera recursiva, probando tanto la división directa como la división intercambiada.

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Verificar si las cadenas son exactamente iguales
        if s1 == s2:
            return True

        # Si las cadenas no tienen los mismos caracteres, no pueden ser scrambles
        if sorted(s1) != sorted(s2):
            return False

        # Usamos un diccionario para la memoización (evitar recomputaciones)
        memo = {}

        def helper(s1, s2):
            # Si ya hemos calculado esta combinación, retornamos el resultado guardado
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            # Si las cadenas son iguales, es un scramble
            if s1 == s2:
                return True

            n = len(s1)

            # Intentamos dividir las cadenas en dos partes
            for i in range(1, n):
                # Caso 1: No se realiza swap
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # Caso 2: Se realiza swap
                if helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    return True

            # Si no encontramos una solución, guardamos el resultado y retornamos False
            memo[(s1, s2)] = False
            return False

        return helper(s1, s2)

# Example 1:
s1 = "great"
s2 = "rgeat"
# Output: true
print(Solution().isScramble(s1, s2))

# Example 2:
s1 = "abcde"
s2 = "caebd"
# Output: false
print(Solution().isScramble(s1, s2))

# Example 3:
s1 = "a"
s2 = "a"
# Output: true
print(Solution().isScramble(s1, s2))
