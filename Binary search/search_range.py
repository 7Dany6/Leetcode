class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in set(nums) or not nums: # here we look for base cases
            return [-1, -1]
			"""
			Our algorithm will take logn in terms of big O notation cause each time we reduce the zone of our search two times
			"""
        l = 0 # set left boarder for our search
        r = len(nums) - 1 # set right boarder
        def left_search(l, r, sequence, target):  # this search will give us an index of the first entrance
            while l < r:
                m = (l + r) // 2 # each time we find a middle between ywo boarders
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l # finally our boarders come to one and we return this value
        def right_search(l, r, sequence, target): # this search will give us an index of the last entrance
            while l < r:
                m = (l + r + 1) // 2
                if nums[m] <= target:
                    l = m
                else:
                    r = m - 1
            return l
        return [left_search(l, r, nums, target), right_search(l, r, nums, target)] # here we return two values 