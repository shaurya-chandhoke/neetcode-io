class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set(nums)
        return len(nums) != len(unique_elements)