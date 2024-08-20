#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

#The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#Example 1:
#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]
#Explanation:
#2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#7 is a candidate, and 7 = 7.
#These are the only two combinations.

#Example 2:
#Input: candidates = [2,3,5], target = 8
#Output: [[2,2,2,2],[2,3,3],[3,5]]

#Example 3:
#Input: candidates = [2], target = 1
#Output: []

#Constraints:
#1 <= candidates.length <= 30
#2 <= candidates[i] <= 40
#All elements of candidates are distinct.
#1 <= target <= 40

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def Backtracking(start_index, current_sum, combination):
            if current_sum == target:
                results.append(list(combination))
                return
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                num = candidates[i]
                combination.append(num)
                Backtracking(i, current_sum + num, combination)
                combination.pop()

        results = [] #combinaciones válidas que suman el target
        Backtracking(0, 0, [])
        return results

#Example 1:
candidates = [2,3,6,7]
target = 7
#Output: [[2,2,3],[7]]
print(Solution().combinationSum(candidates, target))

#Example 2:
candidates = [2,3,5]
target = 8
#Output: [[2,2,2,2],[2,3,3],[3,5]]
print(Solution().combinationSum(candidates, target))

#Example 3:
candidates = [2]
target = 1
#Output: []
print(Solution().combinationSum(candidates, target))
