class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        preffix_sum = [0] * (len(nums) + 1)

        for i in range(1, len(preffix_sum)):
            preffix_sum[i] = preffix_sum[i - 1] + nums[i - 1]

        return 1 - min(preffix_sum)
    