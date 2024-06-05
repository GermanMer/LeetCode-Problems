#Given an integer x, return true if x is a palindrome, and false otherwise.

#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.

#Example 2:
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

#Example 3:
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

#Constraints: -231 <= x <= 231 - 1

#Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Check if the number is negative. If it's negative, it cannot be a palindrome.
        if x < 0:
            return False

        #We initialize two variables
        reversed_num = 0    #This variable will store the reversed value of the number x.
        temp = x            #This variable is a temporary placeholder to manipulate the input number without modifying the original value.

        while temp != 0:    #We enter a loop that continues until temp becomes zero.
            digit = temp % 10   #Extract the last digit of temp using the modulo operator % and store it in the digit variable.
            reversed_num = reversed_num * 10 + digit #To reverse the number, we multiply the current value of reversed by 10 and add the extracted digit.
            temp //= 10     #We then divide temp by 10 to remove the last digit and move on to the next iteration.

        return reversed_num == x #Now, we compare the reversed value reversed with the original input value x.

#!!!The code uses a long long data type for the reversed variable to handle potential overflow in case of large input numbers.

#Example 1:
x = 121
print(Solution().isPalindrome(x))

#Example 2:
x = -121
print(Solution().isPalindrome(x))

#Example 3:
x = 10
print(Solution().isPalindrome(x))
