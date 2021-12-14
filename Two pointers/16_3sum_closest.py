class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 1000000

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = sum([nums[i], nums[left], nums[right]])

                if total == target:
                    return total
                elif abs(target - total) < abs(target - closest):
                    closest = total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest

