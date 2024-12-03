# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path.copy())  # Agregar el subconjunto actual
            for i in range(start, len(nums)):
                path.append(nums[i])  # Agregar el valor actual
                backtrack(i + 1, path)
                path.pop()  # Deshacer la elección

        backtrack(0, []) # Inicia la generación de subconjuntos desde el primer elemento con un camino vacío
        return result

# Example 1:
nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(Solution().subsets(nums))

# Example 2:
nums = [0]
# Output: [[],[0]]
print(Solution().subsets(nums))
