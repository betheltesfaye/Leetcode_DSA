class Solution:
    def check(self, nums: List[int]) -> bool:
        ogNums = sorted(nums)
        firstBlock = []
        lastBlock = []
        
        # Loop through the array to find the "drop"
        for i in range(len(nums) - 1):
            currentVal = nums[i]
            nextVal = nums[i + 1]
            
            if currentVal <= nextVal:
                lastBlock.append(currentVal)
            else:
                lastBlock.append(currentVal)
                firstBlock = nums[(i+1):]
                # Once you find the split point, you can stop 
                # or just collect the rest.
                break 
        
        # FIX: The loop skipped the very last element. 
        # If we didn't find a drop (list is already sorted), 
        # the last element belongs in lastBlock.
        if not firstBlock:
            lastBlock.append(nums[-1])
            
        print(f"firstBlock: {firstBlock}, Last Block: {lastBlock}")

        if (firstBlock + lastBlock) == ogNums:
            return True
        else:
            return False
        
        # Now you can perform your check by combining them
        # ...