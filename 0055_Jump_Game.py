# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# Enfoque: Para resolver el problema de determinar si puedes llegar al último índice de un array nums, donde cada elemento representa la longitud máxima de salto que puedes dar desde esa posición, puedes utilizar un enfoque basado en la greedy algorithm (algoritmo codicioso). La idea principal es mantener un rastreo del índice más lejano que puedes alcanzar en cada paso y actualizarlo según avanzas.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # Inicializa la variable max_reachable en 0

        for i in range(len(nums)):
            if i > max_reachable:
                return False  # No se puede alcanzar el índice i
            max_reachable = max(max_reachable, i + nums[i])  # Actualiza el índice más lejano alcanzable

            if max_reachable >= len(nums) - 1:  # Verifica si podemos alcanzar el último índice
                return True

        return False  # Si no se ha alcanzado el último índice, retorna False

# Example 1:
nums = [2,3,1,1,4]
# Output: true
print(Solution().canJump(nums))

# Example 2:
nums = [3,2,1,0,4]
# Output: false
print(Solution().canJump(nums))
