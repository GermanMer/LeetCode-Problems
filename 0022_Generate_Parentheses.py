#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#Example 1:
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]

#Example 2:
#Input: n = 1
#Output: ["()"]

#Constraints:
#1 <= n <= 8

# Enfoque recursivo (o de backtracking)
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(S = '', left = 0, right = 0): #Se crea la función backtrack, que usa una cadena S para construir las combinaciones mientras que left y right representan el número de paréntesis abiertos y cerrados que se han añadido hasta ahora.
            if len(S) == 2 * n: #Cuando la longitud de S es igual a 2 * n, significa que hemos generado una combinación váliday la añadimos a result.
                result.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right) #Si el número de paréntesis abiertos left es menor que n, añadimos un paréntesis abierto.
            if right < left:
                backtrack(S + ')', left, right + 1) #Si el número de paréntesis cerrados right es menor que el número de paréntesis abiertos, añadimos un paréntesis cerrado.

        result = [] #Lista para almacenar todas las combinaciones válidas de paréntesis
        backtrack() #Llamamos a la función de backtracking por primera vez con una cadena vacía y contadores de paréntesis abiertos y cerrados en 0
        return result

#Example 1:
n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(n))

#Example 2:
n = 1
#Output: ["()"]
print(Solution().generateParenthesis(n))
