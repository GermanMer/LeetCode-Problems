#Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

#Example 1:
#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".

#Example 2:
#Input: s = ")()())"
#Output: 4
#Explanation: The longest valid parentheses substring is "()()".

#Example 3:
#Input: s = ""
#Output: 0

#Constraints:
#0 <= s.length <= 3 * 104
#s[i] is '(', or ')'.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Inicializamos la pila con -1 para manejar el caso base
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':  # Si encontramos un paréntesis de apertura, lo agregamos a la pila
                stack.append(i)
            else:
                stack.pop()  # Si encontramos un paréntesis de cierre, sacamos el último elemento de la pila
                if not stack:
                    stack.append(i)  # Si la pila está vacía, agregamos el índice actual
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculamos la longitud del subcadena válida

        return max_length

#Example 1:
s = "(()"
#Output: 2
print(Solution().longestValidParentheses(s))

#Example 2:
s = ")()())"
#Output: 4
print(Solution().longestValidParentheses(s))

#Example 3:
s = ""
#Output: 0
print(Solution().longestValidParentheses(s))
