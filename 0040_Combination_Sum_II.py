#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

#Each number in candidates may only be used once in the combination.

#Note: The solution set must not contain duplicate combinations.

#Example 1:
#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output:
#[
#[1,1,6],
#[1,2,5],
#[1,7],
#[2,6]
#]

#Example 2:
#Input: candidates = [2,5,2,1,2], target = 5
#Output:
#[
#[1,2,2],
#[5]
#]

#Constraints:
#1 <= candidates.length <= 100
#1 <= candidates[i] <= 50
#1 <= target <= 30

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def Backtracking(start_index, current_sum, combination):
            if current_sum == target:
                if set(list(combination)) not in duplicates:
                    results.append(list(combination))
                    duplicates.append(set(list(combination)))
                    return
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                num = candidates[i]
                combination.append(num)
                Backtracking(i + 1, current_sum + num, combination)
                combination.pop()

        results = [] #combinaciones válidas que suman el target
        duplicates = []
        Backtracking(0, 0, [])
        return results

#Example 1:
candidates = [10,1,2,7,6,1,5]
target = 8
#Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
print(Solution().combinationSum2(candidates, target))

#Example 2:
candidates = [2,5,2,1,2]
target = 5
#Output: [[1,2,2],[5]]
print(Solution().combinationSum2(candidates, target))
