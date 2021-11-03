class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 or not nums:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            right = len(nums) - 1
            left = i + 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return res
