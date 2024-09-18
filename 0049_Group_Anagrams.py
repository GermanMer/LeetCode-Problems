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
        if strs == [""]:
            return [[""]]

        result = []
        stack = []
        count = -1

        for i in strs:
            count = count + 1
            result.append([])
            #mapear las letras en el diccionario
            current = dict()
            for c in i:
                if c not in current:
                    current[c] = 1
                else:
                    current[c] = current[c] +1
            #print(current)

                for x in strs[strs.index(i):]:
                    #mapear las letras en el diccionario
                    others = dict()
                    for o in x:
                        if o not in others:
                            others[o] = 1
                        else:
                            others[o] = others[o] + 1
                    #print(others)

                    #comparar el diccionario others con el diccionario current
                    if others == current and x not in stack:
                        result[count].append(x)
                        stack.append(x)

        for r in result[:]: # Creamos una copia de result con result[:] para evitar los problemas asociados a modificar la lista result mientras se la recorre
            if len(r) < 1:
                result.remove(r)

        return result

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
