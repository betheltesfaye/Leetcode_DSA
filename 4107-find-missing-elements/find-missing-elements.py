class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        minNum = min(nums)
        maxNum = max(nums)
        missNums = []
        
        for i in range(minNum, maxNum):
            if i not in nums:
                missNums.append(i)

        return missNums

        # print(nums)
        # print(minNum)
        # print(maxNum)
        