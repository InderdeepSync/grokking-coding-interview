
def max_sub_array_of_size_k(k, nums):
    end = k
    max_sum = prev_sum = sum(nums[end - k: end])

    lower, upper = 0, end

    end += 1
    while end <= len(nums):
        current_sum = prev_sum - nums[end - k - 1] + nums[end - 1]

        if current_sum > max_sum:
            max_sum = current_sum
            lower = end - k
            upper = end

        prev_sum = current_sum
        end += 1

    return sum(nums[lower: upper])



