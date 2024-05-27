#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R

#And then read line by line: "PAHNAPLSIIGYIR"

#Write the code that will take a string and make this conversion given a number of rows:
#string convert(string s, int numRows)

#Example 1:
#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#Explanation:
#P   A   H   N
#A P L S I I G
#Y   I   R

#Example 2:
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I

#Example 3:
#Input: s = "A", numRows = 1
#Output: "A"

#Constraints:
#1 <= s.length <= 1000
#s consists of English letters (lower-case and upper-case), ',' and '.'.
#1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        index, step = 0, 1

        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(rows)

# Example 1:
s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))

# Example 2:
s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows))

# Example 3:
s = "A"
numRows = 1
print(Solution().convert(s, numRows))




#0 1 2 3  4 5 6 7 8 9  10 11 12 13
#P A Y P  A L I S H I  R  I  N  G
#1 2 3 2  1 2 3 2 1 2  3  2  1  2
#P A H N  A P L S I I  G  Y  I  R
#0 4 8 12 1 3 5 7 9 11 13 2  6  10
