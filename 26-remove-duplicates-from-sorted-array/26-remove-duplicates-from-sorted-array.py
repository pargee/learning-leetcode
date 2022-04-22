class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Another revision, this time a bit cleaner to read
        duplicates = 0
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                duplicates = duplicates + 1
            else:
                nums[index - duplicates] = nums[index]
        return len(nums) - duplicates
                
                