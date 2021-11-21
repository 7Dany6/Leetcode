class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        compare_with = 1
        for num in nums:
            if num == compare_with:
                compare_with += 1
        return compare_with
