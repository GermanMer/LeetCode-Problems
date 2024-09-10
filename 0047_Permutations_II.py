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

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, restantes):
            if not restantes:
                permutaciones.append(path)
                return

            for i in range(len(restantes)):
                backtrack(path + [restantes[i]], restantes[:i] + restantes[i+1:])

        permutaciones = []
        backtrack([], nums)

        # Elimina duplicados
        permUnicas = []
        for perm in permutaciones:
            if perm not in permUnicas:
                permUnicas.append(perm)

        return permUnicas

#Example 1:
nums = [1,1,2]
#Output: [[1,1,2], [1,2,1], [2,1,1]]
print(Solution().permuteUnique(nums))

#Example 2:
nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permuteUnique(nums))
