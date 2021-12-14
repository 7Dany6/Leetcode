class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = max(nums) - min(nums) + 1
        counting_array = [0] * k
        minimum = min(nums)
        for i in range(len(nums)):
            counting_array[nums[i] - minimum] += 1
        pos = 0
        for i in range(k):
            for _ in range(counting_array[i]):
                nums[pos] = i + minimum
                pos += 1
