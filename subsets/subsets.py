
def find_subsets(nums): # Verified on Leetcode
    subsets = [[]]
    for num in nums:
        temp = len(subsets) - 1
        while temp >= 0:
            subsets.append([*subsets[temp], num])
            temp -= 1


    return subsets


if __name__ == "__main__":
    print(find_subsets([2, 5, 7]))