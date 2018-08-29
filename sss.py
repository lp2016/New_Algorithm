def search(nums,key):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    if nums[mid] == key and nums[mid-1] != key:
        return
def get_first_k(nums,key):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == key:
            if (mid >=1 and nums[mid - 1] != key) or mid == 0:
                return mid
            else:
                right = mid - 1
        elif nums[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def get_last_k(nums,key):
    left = 0
    right = len(nums) - 1
    mid = (left+right) // 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == key:
            if (mid <= len(nums) - 2 and nums[mid+1] != key) or mid == len(nums) - 1:
                return mid
            else:
                left = mid + 1
        elif nums[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(get_first_k([1,2],1))


