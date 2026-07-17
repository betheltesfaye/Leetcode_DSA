class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(0, len(nums)-1):
        #     if nums[i] == 0:
        #         zero = nums[i]
        #         nums = nums[i+1:]
        #         nums.append(zero)
        
        # print(nums)

        # Keep all non-zeros, then add a list of zeros matching the count

        # The [:] tells Python to overwrite the existing list in memory
        nums[:] = [x for x in nums if x != 0] + [0] * nums.count(0)

        print(nums)