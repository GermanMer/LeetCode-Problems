#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#Example 1:
#Input: x = 123
#Output: 321

#Example 2:
#Input: x = -123
#Output: -321

#Example 3:
#Input: x = 120
#Output: 21

#Constraints: -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        rev = str(x)
        if rev[0] == "-":
            rev = rev[::-1]
            rev = "-" + rev[:-1]
            rev = int(rev)
        else:
            rev = rev[::-1]
            rev = int(rev)
        if rev.bit_length() <= 32:
            return rev
        else:
            return 0

#Example 1:
x = 123
#Output: 321
print(Solution().reverse(x))

#Example 2:
x = -123
#Output: -321
print(Solution().reverse(x))

#Example 3:
x = 120
#Output: 21
print(Solution().reverse(x))
