# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n = len(nums1)
        insterstion = []

        for i in range(n):
            if nums1[i] in nums2:
                insterstion.append(nums1[i])
                nums2.remove(nums1[i])
        return insterstion
                
