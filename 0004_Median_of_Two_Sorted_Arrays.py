#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

#Example 1:
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.0
#Explanation: merged array = [1,2,3] and median is 2.

#Example 2:
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.5
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, arr1, arr2):
        total_length = len(arr1) + len(arr2)
        if total_length == 0:
            return None
        arr1.extend(arr2)
        arr1.sort()
        if len(arr1) % 2 == 0:
            middle = int(len(arr1) / 2)
            return ((arr1[middle - 1] + arr1[middle]) / 2)
        else:
            return float((arr1[len(arr1) // 2]))

#Example 1:
nums1 = [1,3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))
#Output: 2.0

#Example 2:
nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))
#Output: 2.5

#Example 3:
nums1 = [1,1,1,1,1,36]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))
#Output: 1.0
