#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:
    #Open brackets must be closed by the same type of brackets.
    #Open brackets must be closed in the correct order.
    #Every close bracket has a corresponding open bracket of the same type.

#Example 1:
#Input: s = "()"
#Output: true

#Example 2:
#Input: s = "()[]{}"
#Output: true

#Example 3:
#Input: s = "(]"
#Output: false

#Constraints:
#1 <= s.length <= 104
#s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Utilizamos una lista como pila para almacenar los paréntesis de apertura

        bracket_map = {')': '(', '}': '{', ']': '['} # Diccionario que mapea cada paréntesis de cierre a su correspondiente paréntesis de apertura

        for char in s: # Recorremos cada carácter de la cadena `s`
            if char in bracket_map: # Si el carácter es un paréntesis de cierre
                top_element = stack.pop() if stack else '#' # Extraemos el último elemento de la pila si la pila no está vacía, de lo contrario asignamos un valor de marcador
                # La expresión if stack verifica si la pila no está vacía.
                # Si la pila no está vacía (stack evalúa como True), se puede hacer pop de la pila de manera segura para obtener el último paréntesis de apertura agregado.
                # Si stack está vacía (else), asigna un valor de marcador '#' a top_element, que se utiliza para manejar el caso en el que intentamos verificar un paréntesis de cierre sin un paréntesis de apertura correspondiente en la pila. Este valor de marcador no coincide con ningún paréntesis de apertura válido ('(', '{', '['), por lo que la comparación if bracket_map[char] != top_element: fallará, y la función retornará False, indicando que la cadena no es válida.

                if bracket_map[char] != top_element: # Verificamos si el paréntesis de apertura extraído de la pila coincide con el paréntesis de apertura correspondiente en `bracket_map`
                    return False
            else:
                stack.append(char) # Si el carácter es un paréntesis de apertura, lo agregamos a la pila

        return not stack # Al final, si la pila está vacía, significa que todos los paréntesis de apertura han sido emparejados correctamente y la cadena es válida

#Example 1:
s = "()"
#Output: true
print(Solution().isValid(s))

#Example 2:
s = "()[]{}"
#Output: true
print(Solution().isValid(s))

#Example 3:
s = "(]"
#Output: false
print(Solution().isValid(s))
