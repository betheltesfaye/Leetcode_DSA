class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = []
        for i in nums:
            final.append(i**2)
        sNums = sorted(final)
        return sNums
        