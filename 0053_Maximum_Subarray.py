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

#Enfoque de algoritmo de Kadane:

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Inicializamos las variables para la suma máxima y la suma actual
        max_sum = float('-inf') # float('-inf') representa el infinito negativo, es una manera de decir que un valor es "menor que cualquier otro valor posible". Se usa comúnmente para inicializar variables que deben ser actualizadas con valores mayores o menores durante el cálculo.
        current_sum = 0

        # Recorremos el arreglo
        for num in nums:
            # Actualizamos la suma actual
            current_sum = max(num, current_sum + num)

            # Actualizamos la suma máxima
            max_sum = max(max_sum, current_sum)

        return max_sum

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
