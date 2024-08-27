#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

#Example 1:
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

#Example 2:
#Input: height = [4,2,0,3,2,5]
#Output: 9

#Constraints:
#n == height.length
#1 <= n <= 2 * 104
#0 <= height[i] <= 105

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        #print("start")
        result = 0
        ind = 0
        left = height[ind]
        for i in range(len(height) - 1):
            right = max(height[ind + 1 : ])
            #print("right", right)
            #print("left",left)
            if height[i] < left:
                result = result + (left - height[i])
                #print(result)
            if height[ind] > left and right >= height[ind]:
                left = height[ind]
            ind = ind + 1

        return result

#Example 1:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
print(Solution().trap(height))

#Example 2:
height = [4,2,0,3,2,5]
#Output: 9
print(Solution().trap(height))
