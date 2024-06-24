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
        nums.sort()  # Ordenamos el array para poder utilizar la técnica de dos punteros
        totals = []  # Lista para almacenar todas las sumas posibles de tripletas

        for i in range(len(nums) - 2):  # Iterar hasta len(nums) - 2 para evitar desbordamientos de índice
            left, right = i + 1, len(nums) - 1  # Inicializar los punteros left y right

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                totals.append(current_sum)  # Almacenar la suma actual

                # Mover los punteros según la comparación con el target
                if current_sum < target:
                    left += 1  # Incrementar left para aumentar la suma
                elif current_sum > target:
                    right -= 1  # Decrementar right para disminuir la suma
                else:
                    return current_sum  # Si encontramos una suma exacta, retornamos inmediatamente

        # Encontrar el valor más cercano al target en totals
        if target in totals:
            result = target
        elif len(totals) == 1:
            result = totals[0]
        else:
            totals.append(target)
            totals.sort()
            target_index = totals.index(target)
            if target_index == 0:
                result = totals[1]
            elif target_index == len(totals) - 1:
                result = totals[-1]
            else:
                if target - totals[target_index - 1] < totals[target_index + 1] - target:
                    result = totals[target_index - 1]
                else:
                    result = totals[target_index + 1]

        return result

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
