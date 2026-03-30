class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_table = {}
        for i, el in enumerate(nums):
            diff = target - el
            if diff in lookup_table:
                return [lookup_table[diff], i]
            
            lookup_table[el] = i

        return []