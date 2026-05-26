# class Solution:
#     def numberGame(self, nums: List[int]) -> List[int]:
#         arr = []
#         alice = []
#         bob = []
#         for i in range(len(nums)):
#             alice = [min(nums)]
#             bob = [min(nums)] 
#             nums.remove(alice)
#             nums.remove(bob)
#             arr.append(bob)
#             arr.append(alice)
        
#         print(arr)

# from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # 1. Sort the array so the smallest numbers come first
        nums.sort()
        arr = []
        
        # 2. Iterate by jumping 2 steps at a time
        for i in range(0, len(nums), 2):
            alice = nums[i]
            bob = nums[i + 1]
            
            # 3. Append Bob's move first, then Alice's move
            arr.append(bob)
            arr.append(alice)
            
        return arr                