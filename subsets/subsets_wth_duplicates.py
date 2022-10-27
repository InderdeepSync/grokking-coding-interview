
def find_subsets_with_duplicates(nums):
    nums.sort()

    subsets = [[]]
    for index, num in enumerate(nums):
        temp = len(subsets) - 1
        while temp >= 0:
            if index == 0 or num != nums[index - 1] or subsets[temp].count(num):
                new_subset = [*subsets[temp], num]
                if not subsets.count(new_subset):
                    subsets.append(new_subset)

            temp -= 1

    return subsets


if __name__ == "__main__":
    print(find_subsets_with_duplicates([1, 3, 3]))