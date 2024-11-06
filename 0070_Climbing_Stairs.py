# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        a = 1 # f(1)
        b = 2 # f(2)
        for i in range(3, n + 1):
            c = a + b  # f(n) = f(n-1) + f(n-2)
            a = b      # Actualiza f(n-1)
            b = c      # Actualiza f(n)

        return b  # f(n)

# Example 1:
n = 2
# Output: 2
print(Solution().climbStairs(n))

# Example 2:
n = 3
# Output: 3
print(Solution().climbStairs(n))

# Example 2:
#n = 6
# Output: 28
#print(Solution().climbStairs(n))
