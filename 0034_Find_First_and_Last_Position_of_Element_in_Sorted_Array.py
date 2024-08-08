#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.

#Example 1:
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]

#Example 2:
#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]

#Example 3:
#Input: nums = [], target = 0
#Output: [-1,-1]

#Constraints:
#0 <= nums.length <= 105
#-109 <= nums[i] <= 109
#nums is a non-decreasing array.
#-109 <= target <= 109

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        try:
            result[0] = nums.index(target)
        except:
            return result

        counter = nums.index(target)
        result[1] = counter
        for i in range(len(nums) - counter):
            if nums[counter] == nums[counter + 1]:
                result[1] = counter + 1
                counter = counter +1

        return result

#Example 1:
nums = [5,7,7,8,8,10]
target = 8
#Output: [3,4]
print(Solution().searchRange(nums, target))

#Example 2:
nums = [5,7,7,8,8,10]
target = 6
#Output: [-1,-1]
print(Solution().searchRange(nums, target))

#Example 3:
nums = []
target = 0
#Output: [-1,-1]
print(Solution().searchRange(nums, target))
