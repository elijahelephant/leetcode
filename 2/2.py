class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, value in enumerate(nums):
            c = target - value
            if (c) in num_to_index:
                return [num_to_index[c],index]
            
            else:
                num_to_index[value] = index

