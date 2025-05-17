# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                   
                    while mid > 0 and arr[mid - 1] == target:
                        mid -= 1
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

      
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        result = []
        for num in nums1:
            idx = binary_search(nums2, num)
            if idx != -1:
                result.append(num)
                nums2.pop(idx)  # remove matched number to avoid reuse

        return result
