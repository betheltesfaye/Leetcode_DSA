class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        currentLeftSum = 0
        rightSum = []
        currentRightSum = 0
        final = []
        for i in (range(len(nums))):
            # if i == 0:
            #     leftSum += [0]
            if i == len(nums):
                rightSum.append(nums[i])
                rightSum += [0]
            
            currentLeftSum = sum(nums[: i])
            leftSum.append(currentLeftSum)

            currentRightSum = sum(nums[i+1:])
            rightSum.append(currentRightSum)

        print(leftSum)
        print(rightSum)

        for i in range(len(leftSum)):
            final.append(abs(leftSum[i] - rightSum[i]))
        print(final) 

        return final    

