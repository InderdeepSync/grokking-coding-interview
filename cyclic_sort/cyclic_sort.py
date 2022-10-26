from subsets.subsets import find_subsets


def cyclic_sort(nums):
    index = 0
    while index < len(nums):
        if nums[index] == index + 1:
            index += 1
        else:
            index_to_swap = nums[index] - 1
            nums[index], nums[index_to_swap] = nums[index_to_swap], nums[index]


if __name__ == "__main__":
    input_arr = [1, 5, 6, 4, 3, 2]
    cyclic_sort(input_arr)
    print(input_arr)
