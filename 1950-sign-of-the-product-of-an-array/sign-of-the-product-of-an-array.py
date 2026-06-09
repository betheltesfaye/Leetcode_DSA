class Solution:
    def arraySign(self, nums: List[int]) -> int:
        signFunc = 1
        for i in nums:
            signFunc *= i
        if signFunc == 0:
            return 0
        elif signFunc > 0:
            return 1
        else:
            return -1    