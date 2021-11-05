class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 or not nums:  # at first, we always remember about base cases
            return []
        res = []  # here we are creating a variable for future result
        nums.sort()  # one rule: if you have a sequence and no idea - then sort it, it will take O(nlogn) as python uses quick sort
        for i in range(
                len(nums) - 2):  # we are going through all length except two last element, cause we will create pointers which will point at these values
            right = len(nums) - 1  # here we create our right pointer
            left = i + 1  # here we create our left pointer
            while left < right:  # necessary condition, when they collide, we're moving to another i
                total = nums[i] + nums[left] + nums[right]  # we're checking sum of out three elements
                if total == 0:
                    if [nums[i], nums[left], nums[
                        right]] not in res:  # we need only unique trios, so we should check whether we've encountered this combination before or not
                        res.append([nums[i], nums[left], nums[right]])  # if not - then we append it to our result
                    left += 1  # increase left pointer by 1
                    right -= 1  # and decrease right pointer by 1 as we need to check other numbers
                elif total < 0:  # if total is less than 0, it means that we should sum up bigger value, as we have sorted array, we can move left pointer on its right to get a bigger value
                    left += 1
                elif total > 0:  # and we use the same logic if total is greater than 0
                    right -= 1
        return res
