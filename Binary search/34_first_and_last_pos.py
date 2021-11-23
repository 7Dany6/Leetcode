class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in set(nums):
            return [-1, -1]
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1

        def left_search(l, r, sequence, target):
            while l < r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        def right_search(l, r, sequence, target):
            while l < r:
                m = (l + r + 1) // 2
                if nums[m] <= target:
                    l = m
                else:
                    r = m - 1
            return l

        return [left_search(l, r, nums, target), right_search(l, r, nums, target)]
