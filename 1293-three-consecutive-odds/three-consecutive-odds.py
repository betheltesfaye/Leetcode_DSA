class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(2, len(arr)):
            value = False
            if (arr[i] % 2 != 0) and (arr[i-1] % 2 != 0) and (arr[i-2] % 2 != 0):
                print(arr[i], arr[i-1], arr[i-2])
                return True
        return False