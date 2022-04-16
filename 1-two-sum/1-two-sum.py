class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     map = {}
    #     for n in range(len(nums)):
    #         difference = target - nums[n]
    #         if difference in map:
    #             return [map[difference], n]
    #         map[nums[n]] = n
    #     return None
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentials = []
        for n in range(len(nums)):
            difference = target - nums[n]
            if difference in potentials:
                return [potentials.index(difference), n]
            potentials.append(nums[n])
        return None