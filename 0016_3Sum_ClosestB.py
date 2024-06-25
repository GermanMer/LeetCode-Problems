#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

#Return the sum of the three integers.

#You may assume that each input would have exactly one solution.

#Example 1:
#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

#Example 2:
#Input: nums = [0,0,0], target = 1
#Output: 0
#Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

#Constraints:
#3 <= nums.length <= 500
#-1000 <= nums[i] <= 1000
#-104 <= target <= 104

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()  # Ordenar el array
        closest_sum = float('inf')  # Inicializar con infinito

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Actualizar la suma más cercana
                if abs(current_sum - target) < abs(closest_sum - target): # La función abs() devuelve el valor absoluto de un número, es decir, la distancia del número desde cero en una recta numérica, sin importar si el número es positivo o negativo.
                    closest_sum = current_sum

                # Mover los punteros
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Si encontramos la suma exacta

        return closest_sum

#Example 1:
nums = [-1,2,1,-4]
target = 1
#Output: 2
print(Solution().threeSumClosest(nums, target))

#Example 2:
nums = [0,0,0]
target = 1
#Output: 0
print(Solution().threeSumClosest(nums, target))
