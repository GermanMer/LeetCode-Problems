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
        stack = [] # Utilizamos una lista como pila para almacenar los paréntesis de apertura
        result = ""
        bracket_map = {')': '('} # Diccionario que mapea cada paréntesis de cierre a su correspondiente paréntesis de apertura

        for char in s: # Recorremos cada carácter de la cadena `s`
            if char in bracket_map: # Si el carácter es un paréntesis de cierre
                if stack: # si la pila no está vacía
                    top_element = stack.pop() # Extraemos el último elemento de la pila
                    result = result + "()"
                else: continue
            else:
                stack.append(char) # Si el carácter es un paréntesis de apertura, lo agregamos a la pila

        #print(result)
        return len(result)

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
