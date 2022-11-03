
def lengthOfLongestSubstring(input_string: str) -> int: # More Efficient Solution
    last_seen = {}
    start_index = 0
    current_longest_substring = (0, 1)
    for index, char in enumerate(input_string):
        if char in last_seen:
            start_index = max(start_index, last_seen[char] + 1)

        if current_longest_substring[1] - current_longest_substring[0] < (index + 1) - start_index:
            current_longest_substring = (start_index, index + 1)

        last_seen[char] = index

    return len(input_string[current_longest_substring[0]: current_longest_substring[1]])

def lengthOfLongestSubstringSlidingWindow(str1: str) -> int: # Accepted on leetcode
    start = end = 0
    window_info = {}
    result = 0

    def are_window_characters_unique():
        for ch, freq in window_info.items():
            if freq > 1:
                return False

        return True

    while start != len(str1):
        if end < len(str1) and str1[end] not in window_info:
            window_info[str1[end]] = 1
            if are_window_characters_unique():
                result = max(result, (end + 1) - start)

            end += 1
        else:
            if window_info[str1[start]] > 1:
                window_info[str1[start]] -= 1
                if are_window_characters_unique():
                    result = max(result, end - (start + 1))
            else:
                del window_info[str1[start]]

            start += 1

    return result


if __name__ == "__main__":
    print(lengthOfLongestSubstringSlidingWindow("ohomm"))