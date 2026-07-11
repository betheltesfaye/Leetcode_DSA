class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        finalNum = 0
        finalList = []
        for i in range(len(nums)):
            if nums[i] == target:
                finalNum = abs(i-start)
                finalList.append(finalNum)
        return min(finalList)
            