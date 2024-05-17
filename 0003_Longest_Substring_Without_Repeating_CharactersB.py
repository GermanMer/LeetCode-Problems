#Given a string s, find the length of the longest substring without repeating characters.

#Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#Example 2:
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.

#Example 3:
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

#Example 1:
string = "abcabcbb"
print(Solution().lengthOfLongestSubstring(string)) #Output: 3

#Example 2:
string = "bbbbb"
print(Solution().lengthOfLongestSubstring(string)) #Output: 1

#Example 3:
string = "pwwkew"
print(Solution().lengthOfLongestSubstring(string)) #Output: 3
