class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        x = 1
        temp_l = []
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] = None
            else:
                x = x + 1
                temp_l.append(nums[index])
        temp_l.append(nums[-1])

        for index in range(len(nums)):
            if index < len(temp_l):
                nums[index] = temp_l[index]
            else:
                nums[index] = None
                
        return x
                
                