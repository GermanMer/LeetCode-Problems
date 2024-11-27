# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Punteros iniciales
        low, mid, high = 0, 0, len(nums) - 1

        # Recorre la lista hasta que mid sobrepase high
        while mid <= high:
            if nums[mid] == 0:
                # Si el elemento es 0, intercámbialo con el elemento en low
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1  # Avanza el puntero low
                mid += 1  # Avanza el puntero mid
            elif nums[mid] == 1:
                # Si el elemento es 1, simplemente avanza mid
                mid += 1
            else:  # nums[mid] es 2
                # Si el elemento es 2, intercámbialo con el elemento en high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1  # Decrementa el puntero high, mid no se incrementa

# Example 1:
nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
Solution().sortColors(nums)
print(nums)

# Example 2:
nums = [2,0,1]
# Output: [0,1,2]
Solution().sortColors(nums)
print(nums)
