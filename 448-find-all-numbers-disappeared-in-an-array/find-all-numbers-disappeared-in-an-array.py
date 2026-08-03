# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         arrayN = []
#         final = []
#         for i in range(1, len(nums)+1):
#             arrayN.append(i)
#         # for i in nums:
#         #     if i < len(nums) and i > 1:
#         #         final.append(i)

#         result = [i for i in arrayN if i not in nums]

#         # print(arrayN)
#         # print(final)  
#         # print(result)

#         return result


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark visited numbers by making the value at their index negative
        for num in nums:
            # Use abs() because the number might have been flipped negative already
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: Any index that is still positive means its corresponding number never appeared
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
                
        return result