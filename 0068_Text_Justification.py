# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

# Example 1:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

# Constraints:
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # Lista para almacenar las líneas justificadas.
        current_line = []  # Lista para la línea actual que se está construyendo.
        current_length = 0  # Longitud acumulada de las palabras en current_line.

        # Iterar sobre cada palabra en la lista de palabras.
        for word in words:
            # Verificar si la longitud actual más la nueva palabra excede maxWidth.
            if current_length + len(word) + len(current_line) > maxWidth:
                # Distribuir espacios entre las palabras de la línea actual.
                for i in range(maxWidth - current_length):
                    # Agregar un espacio al slot correspondiente de current_line.
                    # Utiliza módulo para distribuir los espacios cíclicamente.
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                    # len(current_line): Calcula cuántos espacios pueden distribuirse entre las palabras, por ejemplo, si hay 3 palabras, hay 2 espacios entre ellas.
                    # or 1: Esta parte se asegura de que, si len(current_line) es 1 (es decir, hay solo una palabra), se use 1 en lugar de 0. Esto es importante porque no se pueden distribuir espacios si solo hay una palabra, pero aún se debe asignar al menos un espacio para no provocar una división por cero. En términos simples, si no hay espacios (len(current_line) - 1 sería 0), se usará 1 para evitar errores.
                    # i % (len(current_line) - 1 or 1): Aquí se está utilizando el operador módulo (%) para determinar en qué "slot" (o posición) de current_line se debe añadir el espacio. La expresión se evalúa a un número que varía entre 0 y n - 2 (donde n es el número de palabras) si hay múltiples palabras, o simplemente a 0 si hay una sola palabra. Esto permite que los espacios se distribuyan de manera cíclica entre las posiciones disponibles. Si i es mayor que n - 2, el operador módulo reiniciará la cuenta, asegurando que los espacios se añadan en un patrón cíclico.
                    # += ' ': Finalmente, este operador añade un espacio al slot determinado de current_line. Esto significa que se está distribuyendo un espacio en la posición calculada.

                # Unir las palabras de current_line en una cadena y agregarla a result.
                result.append(''.join(current_line))

                # Reiniciar current_line y current_length para la nueva línea.
                current_line = []
                current_length = 0

            # Agregar la palabra actual a current_line y actualizar la longitud.
            current_line.append(word)
            current_length += len(word)

        # Justificar la última línea a la izquierda.
        result.append(' '.join(current_line).ljust(maxWidth))

        return result  # Retornar el resultado final.

# Example 1:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
print(Solution().fullJustify(words, maxWidth))

# Example 2:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
print(Solution().fullJustify(words, maxWidth))

# Example 3:
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
print(Solution().fullJustify(words, maxWidth))
