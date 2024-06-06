#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).

#Example 1:
#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".

#Example 2:
#Input: s = "aa", p = "a*"
#Output: true
#Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

#Example 3:
#Input: s = "ab", p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".

#Constraints:
#1 <= s.length <= 20
#1 <= p.length <= 20
#s contains only lowercase English letters.
#p contains only lowercase English letters, '.', and '*'.
#It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Memoization dictionary
        memo = {}

        def dp(i, j):
            # Check if the result is already computed
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern is empty, string must also be empty
            if j == len(p):
                return i == len(s)

            # Check if the current character matches
            first_match = i < len(s) and p[j] in {s[i], '.'}

            # If there's a star in the pattern
            if j + 1 < len(p) and p[j + 1] == '*':
                # Consider two cases:
                # 1. We ignore "x*" (move pattern by 2)
                # 2. We use "x*" to match one character (move string by 1)
                result = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # No star, just move both string and pattern by 1
                result = first_match and dp(i + 1, j + 1)

            # Memoize the result
            memo[(i, j)] = result
            return result

        # Start the recursion from the beginning of both the string and the pattern
        return dp(0, 0)

#Example 1:
s = "aa"
p = "a"
print(Solution().isMatch(s, p))
#Output: false

#Example 2:
s = "aa"
p = "a*"
#Output: true
print(Solution().isMatch(s, p))

#Example 3:
s = "ab"
p = ".*"
#Output: true
print(Solution().isMatch(s, p))
