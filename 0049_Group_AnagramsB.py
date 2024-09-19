#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#Example 1:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#Explanation:
#There is no string in strs that can be rearranged to form "bat".
#The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

#Example 2:
#Input: strs = [""]
#Output: [[""]]

#Example 3:
#Input: strs = ["a"]
#Output: [["a"]]

#Constraints:
#1 <= strs.length <= 104
#0 <= strs[i].length <= 100
#strs[i] consists of lowercase English letters.

from typing import List

from collections import defaultdict
# defaultdict es una subclase de dict (diccionario) en el módulo collections de Python. Ofrece una forma conveniente de manejar casos en los que deseas inicializar un diccionario con un valor por defecto para las claves que aún no existen. Esto evita la necesidad de verificar si una clave está en el diccionario antes de agregarle un valor.
#Cómo funciona defaultdict: En lugar de lanzar una excepción cuando accedes a una clave que no existe, un defaultdict crea automáticamente un valor por defecto para esa clave. Puedes especificar el tipo de valor por defecto que deseas al crear el defaultdict.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Diccionario para almacenar las listas de anagramas
        anagram_groups = defaultdict(list)

        for s in strs:
            # Ordenar el string y usarlo como clave
            sorted_str = ''.join(sorted(s))
            # Agregar el string a la lista correspondiente en el diccionario
            anagram_groups[sorted_str].append(s)

        # Devolver los grupos de anagramas como una lista de listas
        return list(anagram_groups.values())

#Example 1:
strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution().groupAnagrams(strs))

#Example 2:
strs = [""]
#Output: [[""]]
print(Solution().groupAnagrams(strs))

#Example 3:
strs = ["a"]
#Output: [["a"]]
print(Solution().groupAnagrams(strs))
