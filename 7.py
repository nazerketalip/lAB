def has_33(nums):
    result = False
    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1] or nums[i-1] == nums[i]) and nums[i]== 3 :
            return True
    return False


n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
print(has_33(arr))



