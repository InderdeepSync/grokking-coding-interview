

def first_missing_positive(nums): # Verified on Leetcode
    index = 0
    while index < len(nums):
        if nums[index] <= 0:
            nums.pop(index)
            continue
        index += 1

    for i in range(len(nums)):
        try:
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        except IndexError:
            pass

    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    return len(nums) + 1


if __name__ == "__main__":
    print(first_missing_positive([3, 4, -1, 1]))