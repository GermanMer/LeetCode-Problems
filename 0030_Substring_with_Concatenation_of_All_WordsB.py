#You are given a string s and an array of strings words. All the strings of words are of the same length.

#A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

#For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
#Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

#Example 1:
#Input: s = "barfoothefoobarman", words = ["foo","bar"]
#Output: [0,9]
#Explanation:
#The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
#The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

#Example 2:
#Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
#Output: []
#Explanation:
#There is no concatenated substring.

#Example 3:
#Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
#Output: [6,9,12]
#Explanation:
#The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
#The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
#The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

#Constraints:
#1 <= s.length <= 104
#1 <= words.length <= 5000
#1 <= words[i].length <= 30
#s and words[i] consist of lowercase English letters.

# Enfoque basado en ventanas deslizantes y conteo de palabras:
#Inicialización: Calculamos la longitud de cada palabra, la cantidad total de palabras, y la longitud de la subcadena objetivo.
#Conteo de palabras: Usamos Counter para contar la frecuencia de cada palabra en words.
#Ventana deslizante: Utilizamos una ventana deslizante para verificar cada posible subcadena de longitud substring_len.
#Conteo de palabras en la ventana: Mantenemos un conteo de las palabras encontradas dentro de la ventana actual y ajustamos la ventana si encontramos una palabra en exceso.
#Verificación de subcadenas: Si la longitud de la ventana es igual a substring_len, hemos encontrado una subcadena válida y añadimos el índice inicial a result.

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Si la cadena s o la lista de palabras está vacía, devolvemos una lista vacía
        if not s or not words:
            return []

        # Longitud de cada palabra
        word_len = len(words[0])
        # Número de palabras en la lista
        num_words = len(words)
        # Longitud total de la subcadena que estamos buscando
        substring_len = word_len * num_words
        # Contador de palabras en la lista
        word_count = Counter(words)
        # Lista para almacenar los índices de las subcadenas válidas
        result = []

        # Iteramos a través de cada posible posición inicial en la cadena s
        for i in range(word_len):
            left = i  # Límite izquierdo de la ventana deslizante
            right = i  # Límite derecho de la ventana deslizante
            current_count = Counter()  # Contador de palabras en la ventana actual

            # Mover la ventana a través de la cadena s
            while right + word_len <= len(s):
                # Obtener la palabra en la posición actual del límite derecho
                word = s[right:right + word_len]
                # Mover el límite derecho hacia adelante
                right += word_len

                if word in word_count:
                    # Si la palabra está en la lista de palabras, la añadimos al contador actual
                    current_count[word] += 1

                    # Si tenemos más instancias de la palabra de las que hay en word_count,
                    # movemos el límite izquierdo para mantener la ventana válida
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len

                    # Si la longitud de la ventana es igual a la longitud de la subcadena,
                    # significa que hemos encontrado una subcadena válida
                    if right - left == substring_len:
                        result.append(left)
                else:
                    # Si la palabra no está en la lista de palabras, reiniciamos el contador y
                    # movemos el límite izquierdo hacia el límite derecho
                    current_count.clear()
                    left = right

        return result

#Example 1:
s = "barfoothefoobarman"
words = ["foo","bar"]
#Output: [0,9]
print(Solution().findSubstring(s, words))

#Example 2:
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
#Output: []
print(Solution().findSubstring(s, words))

#Example 3:
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
#Output: [6,9,12]
print(Solution().findSubstring(s, words))
