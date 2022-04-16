class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using a set to store values since it's lighter than dict
        options = set()
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in options:
                return [nums.index(diff), n]
            options.add(nums[n])
        return None