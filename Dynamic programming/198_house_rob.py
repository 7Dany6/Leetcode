class Solution:
    def rob(self, nums: List[int]) -> int:
        previous = current = 0

        for num in nums:
            temp = previous
            previous = current
            current = max(num + temp, previous)

        return current
    