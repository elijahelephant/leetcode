class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for num in nums:
            if num in myset:
                return True
            else:
                myset.add(num)
        return False