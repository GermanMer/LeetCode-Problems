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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Diccionario para almacenar las listas de anagramas
        anagram_groups = {}

        for s in strs:
            # Ordenar el string y usarlo como clave
            sorted_str = ''.join(sorted(s))

            # Si la clave no existe, crear una nueva lista
            if sorted_str not in anagram_groups:
                anagram_groups[sorted_str] = []

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
