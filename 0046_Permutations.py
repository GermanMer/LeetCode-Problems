#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#Example 1:
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

#Example 2:
#Input: nums = [0,1]
#Output: [[0,1],[1,0]]

#Example 3:
#Input: nums = [1]
#Output: [[1]]

#Constraints:
#1 <= nums.length <= 6
#-10 <= nums[i] <= 10
#All the integers of nums are unique.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, restantes):
            # Si no quedan números restantes, añade la permutación actual al resultado
            if not restantes:
                resultado.append(path)
                return
                # Itera sobre los números restantes
            for i in range(len(restantes)):
                # Realiza un seguimiento de la ruta actual y los números restantes
                backtrack(path + [restantes[i]], restantes[:i] + restantes[i+1:])

        resultado = []
        backtrack([], nums)  # Inicia el backtracking con una ruta vacía y todos los números
        return resultado

#Example 1:
nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute(nums))

#Example 2:
nums = [0,1]
#Output: [[0,1],[1,0]]
print(Solution().permute(nums))

#Example 3:
nums = [1]
#Output: [[1]]
print(Solution().permute(nums))
