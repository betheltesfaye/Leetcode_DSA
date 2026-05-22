class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        y = x + 1
        xList = []
        while x < len(nums):
            while y < len(nums):
                if nums[x] + nums[y] == target:
                    xList.append(x)
                    xList.append(y)
                    return xList
                else:
                    y = y + 1
        
            if y == len(nums):
                x = x + 1
                y = x + 1
                while y < len(nums):
                    if nums[x] + nums[y] == target:
                        xList.append(x)
                        xList.append(y)
                        return xList
                    else:
                        y = y + 1
        else:
            x = x + 1