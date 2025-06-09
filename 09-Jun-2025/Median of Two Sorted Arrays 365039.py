# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        mid = n // 2

        if n % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return float(nums[mid])