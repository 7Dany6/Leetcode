"""
Well, at first glance this problem may see a little bit tricky but let's dive into it.
We've been told that complexity of our algorithm should be O(logn) and the very first thing which pops into our mind - BINARY SEARCH. And here is the main idea:
First of all, we understand that in the array we have pairs and only one element which is single. It means we should point each time at the even index. For that, we'll calculate m as:
m = ((l + r) // 4) * 2
So, for each iteration we calculate a median and imagine the following array:

[1, 2, 2, 3, 3]
At first we should make a check - nums[m] != nums[m - 1] and nums[m + 1]. If it's so - then we return our m and finish search.
Our pointer will point at number 2 with index 2 as well. And we are going to compare it to the right element. Here, they are not equal. Hence, we understand that something went wrong before index 2. What is more, it means that the previous element is the same as current and we can move our right to m-2.
[1, 1, 2, 2, 3]
In this case we again have our pointer pointing at 2 with index 2. But our check shows that the following number is the same and it means that we've already found the pair. And we have the opposite situation to the previous case. Cause now we find out that before found index everything is OK and problem is somewhere further, so lets move our left to m+2
Now we are ready to write a code for our algorithm:
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = ((l + r) // 4) * 2
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m - 2
        return nums[l]
