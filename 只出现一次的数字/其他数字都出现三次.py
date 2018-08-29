def bit(nums):
    sumd = [0]*16     #假设数不超过65536
    for i in range(0,len(nums)):
        tmp = nums[i]
        t = 1
        for j in range(0,16):
            if tmp & t:
                sumd[j] += 1
            t = t << 1
    result = 0
    for i in range(0,16):
        if sumd[i] % 3 == 1:
            result += 2**i
    return result



print(bit([1,1,1,2,3,4,4,2,2,4,5,3,3]))