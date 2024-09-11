#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

#Example 1:
#Input: nums = [1,1,2]
#Output: [[1,1,2], [1,2,1], [2,1,1]]

#Example 2:
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

#Constraints:
#1 <= nums.length <= 8
#-10 <= nums[i] <= 10

from typing import List
import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Genera todas las permutaciones como tuplas
        permutaciones = list(itertools.permutations(nums))

        # Elimina duplicados
        permUnicas = []
        for perm in permutaciones:
            if perm not in permUnicas:
                permUnicas.append(perm)

        # Convierte las tuplas en listas
        resultado = [list(perm) for perm in permUnicas]

        return resultado

#Example 1:
nums = [1,1,2]
#Output: [[1,1,2], [1,2,1], [2,1,1]]
print(Solution().permuteUnique(nums))

#Example 2:
nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permuteUnique(nums))
