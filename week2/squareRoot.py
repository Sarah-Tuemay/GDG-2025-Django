num = 8
left = 1
right = 8
while left <= right:
    mid = left + right // 2
    if mid * mid == num:
        print(mid)
        break
    elif mid * mid < num:
        left += 1
    else:
        right -= 1

         