def sum_of_target(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [3, 2, 4]
print(sum_of_target(nums, 6))