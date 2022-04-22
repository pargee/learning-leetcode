class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Another revision, this time a bit cleaner to read but slower - not sure why
        duplicates = 0
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                duplicates = duplicates + 1
            else:
                # We don't care what the tail values are, so leave and just overwrite the previous duplicate
                # Example, [1, 2, 2, 4] would move 4 to [2] (index = 3, duplicates = 1 or 3 - 1 = [2])
                nums[index - duplicates] = nums[index]
        return len(nums) - duplicates
                
                