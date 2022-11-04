"""
https://leetcode.com/problems/unique-binary-search-trees/

"""

def calculate_tree_count_from_numbers(end): # Accepted on Leetcode
    result = 0

    for index in range(end):
        left_trees_count = optimal_calculator(index) if index != 0 else 1
        right_trees_count = optimal_calculator(end - index - 1) if index != end - 1 else 1

        result += left_trees_count * right_trees_count

    return result


cache = {}
def optimal_calculator(end):
    temp = end
    if temp in cache:
        return cache[temp]

    result = calculate_tree_count_from_numbers(end)
    cache[temp] = result
    return result


if __name__ == "__main__":
    print(optimal_calculator(19))