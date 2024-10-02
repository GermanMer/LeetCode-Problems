#Given an integer array nums, find the subarray with the largest sum, and return its sum.

#Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#Example 2:
#Input: nums = [1]
#Output: 1
#Explanation: The subarray [1] has the largest sum 1.

#Example 3:
#Input: nums = [5,4,-1,7,8]
#Output: 23
#Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

#Constraints:
#1 <= nums.length <= 105
#-104 <= nums[i] <= 104

#Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

#Enfoque de Divide y Vencerás:

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxCrossingSum(nums: List[int], left: int, mid: int, right: int) -> int:
            # Encuentra la suma máxima de la subcadena que cruza el medio
            left_sum = float('-inf')
            right_sum = float('-inf')

            total = 0
            # Suma máxima en la mitad izquierda
            for i in range(mid, left - 1, -1):
                total += nums[i]
                left_sum = max(left_sum, total)

            total = 0
            # Suma máxima en la mitad derecha
            for i in range(mid + 1, right + 1):
                total += nums[i]
                right_sum = max(right_sum, total)

            return left_sum + right_sum

        def maxSubArraySumDivideAndConquer(nums: List[int], left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_sum = maxSubArraySumDivideAndConquer(nums, left, mid)
            right_sum = maxSubArraySumDivideAndConquer(nums, mid + 1, right)
            cross_sum = maxCrossingSum(nums, left, mid, right)

            return max(left_sum, right_sum, cross_sum)

        return maxSubArraySumDivideAndConquer(nums, 0, len(nums) - 1)

#Example 1:
nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
print(Solution().maxSubArray(nums))

#Example 2:
nums = [1]
#Output: 1
print(Solution().maxSubArray(nums))

#Example 3:
nums = [5,4,-1,7,8]
#Output: 23
print(Solution().maxSubArray(nums))
