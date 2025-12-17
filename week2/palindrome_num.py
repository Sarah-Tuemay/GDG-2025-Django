def palindrome_num(num):
    if num < 0:
        return False
    strNum = str(num)
    left = 0
    right = len(strNum)-1
    while(left < right):
        if strNum[left] != strNum[right]:
            return False
        left+=1
        right-=1
    
    return True
    
num = -121
print(palindrome_num(num))