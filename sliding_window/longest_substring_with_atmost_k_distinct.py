
def longest_substring_with_atmost_k_distinct_characters(str1, k): # Accepted on Leetcode [FruitBaskets]
    window_info = {}

    start = end = 0
    result = -1
    while True:
        if len(window_info.keys()) <= k:
            result = max(result, end - start)

            if end == len(str1):
                break

            if str1[end] in window_info:
                window_info[str1[end]] += 1
            else:
                window_info[str1[end]] = 1

            # result = max(result, str1[start: end], key=len)
            end += 1
        else:
            if window_info[str1[start]] > 1:
                window_info[str1[start]] -= 1
            else:
                del window_info[str1[start]]

            start += 1

    return result

def longest_k_unique_characters_substring(str1, k): # Accepted on GeeksForGeeks
    window_info = {}

    start = end = 0
    result = -1
    while True:
        if len(window_info.keys()) <= k:
            if len(window_info.keys()) == k: # This line is the only difference in the two solutions presented here.
                result = max(result, end - start) # The corresponding substring is str[start: end]

            if end == len(str1):
                break

            if str1[end] in window_info:
                window_info[str1[end]] += 1
            else:
                window_info[str1[end]] = 1

            # result = max(result, str1[start: end], key=len)
            end += 1
        else:
            if window_info[str1[start]] > 1:
                window_info[str1[start]] -= 1
            else:
                del window_info[str1[start]]

            start += 1

    return result


if __name__ == "__main__":
    print(longest_substring_with_atmost_k_distinct_characters("araaci", 2))
    print(longest_k_unique_characters_substring("aabacbebebe", 3))