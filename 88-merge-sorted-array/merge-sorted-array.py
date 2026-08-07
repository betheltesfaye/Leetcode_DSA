class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lenDif = len(nums1) - len(nums2)
        for i in nums2:
            # nums1.insert(i, lenDif) 
            nums1[lenDif] = i 
            lenDif += 1

        return nums1.sort() 

        