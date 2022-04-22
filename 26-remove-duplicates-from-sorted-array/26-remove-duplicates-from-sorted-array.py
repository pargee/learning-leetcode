class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Had some trouble figuring out what the actual output was
        # Should try figuring out a different way to sort this
        x = 1
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] = None
            else:
                x = x + 1
        nums.sort(key=lambda x: (x is None, x))
        return x
                
                