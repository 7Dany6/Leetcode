def select_seat(nums: list):
    dist = max_dist = 0
    last_one = None
    for i in range(len(nums)):
        if nums[i] == 1:
            if last_one is None:
                last_one = first_one = i
            if dist > max_dist:
                seat = (i + last_one) // 2
                dist_compare = max(seat - last_one, i - seat)
            max_dist = max(max_dist, dist)
            last_one, dist = i, 0
        dist += 1
    left_dist = first_one
    right_dist = len(nums) - 1 - last_one
    if right_dist > max(left_dist, dist_compare):
        return len(nums) - 1
    elif left_dist > max(right_dist, dist_compare):
        return 0
    return seat
