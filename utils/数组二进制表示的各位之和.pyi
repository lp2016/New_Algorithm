def bit(nums):
    sumd = [0]*16
    for i in range(0,len(nums)):
        tmp = nums[i]
        t = 1
        for j in range(0,16):
            if tmp & t:
                sumd[j] += 1
            t = t << 1
        return sumd
print(bit([1,2,3]))