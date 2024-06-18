#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Example 2:
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.

#Constraints:
#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = strs[0]

        for i in strs[1:]:
            while not i.startswith(result) and result:  # el chequeo len(result) > 0 de la versión anterior es redundante debido a que en Python, una cadena vacía "" se evalúa como False. Aquí se simplifica la condición usando directamente result en lugar de len(result) > 0.
                result = result[:-1]
        return result

#Example 1:
strs = ["flower","flow","flight"]
#Output: "fl"
print(Solution().longestCommonPrefix(strs))

#Example 2:
strs = ["dog","racecar","car"]
#Output: ""
print(Solution().longestCommonPrefix(strs))
