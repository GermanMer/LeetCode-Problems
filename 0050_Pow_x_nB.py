#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

#Example 1:
#Input: x = 2.00000, n = 10
#Output: 1024.00000

#Example 2:
#Input: x = 2.10000, n = 3
#Output: 9.26100

#Example 3:
#Input: x = 2.00000, n = -2
#Output: 0.25000
#Explanation: 2-2 = 1/22 = 1/4 = 0.25

#Constraints:
#-100.0 < x < 100.0
#-231 <= n <= 231-1
#n is an integer.
#Either x is not zero or n > 0.
#-104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

#Example 1:
x = 2.00000
n = 10
#Output: 1024.00000
print(f"{Solution().myPow(x, n):.5f}") # Muestra el resultado con 5 decimales, como se muestra en el ejemplo

#Example 2:
x = 2.10000
n = 3
#Output: 9.26100
print(f"{Solution().myPow(x, n):.5f}")

#Example 3:
x = 2.00000
n = -2
#Output: 0.25000
print(f"{Solution().myPow(x, n):.5f}")
