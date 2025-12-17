def moveZeros(nums):
    left = 0
    right = 0
    while right < len(nums):
        while(nums[left]!=0):
            left+=1
            right+=1
        while(right < len(nums) and nums[right]==0):
            right+=1
        if(right != len(nums)):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

    print(nums)
    
nums = [0, 1, 0, 3, 12]
moveZeros(nums)