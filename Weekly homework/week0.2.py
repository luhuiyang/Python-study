x = int(raw_input('Enter your total number'))
nums = []

def last(x, step):
    if x <= 0 or step <= 1:return 'params error'
    
    temp_step = step - 1
    
    for i in range(x):
        nums.append(i+1)

    while len(nums) > 1:
        if temp_step - len(nums) >=0:
            temp_step = temp_step - len(nums)
        else:
            print temp_step
            print nums
            nums.pop(temp_step)
            temp_step += step -1
    return nums

nums = last(x, 3)

print nums
