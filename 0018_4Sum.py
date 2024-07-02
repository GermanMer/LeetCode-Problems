#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    #0 <= a, b, c, d < n
    #a, b, c, and d are distinct.
    #nums[a] + nums[b] + nums[c] + nums[d] == target

#You may return the answer in any order.

#Example 1:
#Input: nums = [1,0,-1,0,-2,2], target = 0
#Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

#Example 2:
#Input: nums = [2,2,2,2,2], target = 8
#Output: [[2,2,2,2]]

#Constraints:
#1 <= nums.length <= 200
#-109 <= nums[i] <= 109
#-109 <= target <= 109

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        party = set() # Usamos un conjunto para evitar duplicados
        nums.sort() # Ordenamos los números para poder identificar duplicados
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range (k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            party.add((nums[i], nums[j], nums[k], nums[l])) # Agregamos como una tupla al conjunto
                        else: continue
        return [list(group) for group in party]

#Example 1:
nums = [1,0,-1,0,-2,2]
target = 0
#Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(Solution().fourSum(nums, target))

#Example 2:
nums = [2,2,2,2,2]
target = 8
#Output: [[2,2,2,2]]
print(Solution().fourSum(nums, target))
