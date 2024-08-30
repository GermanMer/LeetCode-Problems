#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Example 1:
#Input: num1 = "2", num2 = "3"
#Output: "6"

#Example 2:
#Input: num1 = "123", num2 = "456"
#Output: "56088"

#Constraints:
#1 <= num1.length, num2.length <= 200
#num1 and num2 consist of digits only.
#Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        result = str(num1 * num2)
        #print(type(result))

        return result

#Example 1:
num1 = "2"
num2 = "3"
#Output: "6"
print(Solution().multiply(num1, num2))

#Example 2:
num1 = "123"
num2 = "456"
#Output: "56088"
print(Solution().multiply(num1, num2))
