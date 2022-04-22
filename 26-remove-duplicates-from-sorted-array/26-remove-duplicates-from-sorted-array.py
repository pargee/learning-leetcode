class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Had some trouble figuring out what the actual output was
        # Should try figuring out a different way to sort this
#         x = 1
#         temp_l = []
#         for index in range(len(nums) - 1):
#             if nums[index] == nums[index + 1]:
#                 nums[index] = None
#             else:
#                 x = x + 1
#                 temp_l.append(nums[index])
#         temp_l.append(nums[-1])

#         for index in range(len(nums)):
#             if index < len(temp_l):
#                 nums[index] = temp_l[index]
#             else:
#                 nums[index] = None
                
#         return x
        
        # Surprisingly, this is slower and more memory intensive (140MS / 16.8MB)
        # Way cleaner though...
        x = 1
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] = None
            else:
                x = x + 1
        nums.sort(key=lambda x: (x is None, x))
        return x
                
                