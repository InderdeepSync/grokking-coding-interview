from typing import List


def get_info(words):
    info = {}
    for word in words:
        if word not in info:
            info[word] = 1
        else:
            info[word] += 1

    return info


def find_substring(str1: str, words: List[str]) -> List[int]:
    word_length = len(words[0])
    start = 0
    end = len(words) * word_length

    window_info = get_info(words)

    temp = word_length
    while temp <= end:
        snip = str1[temp - word_length: temp]
        if snip in window_info:
            window_info[snip] -= 1

        temp += word_length

    def does_current_window_contain_concatenation():
        for key in window_info:
            if window_info[key] > 0:
                return False

        return True

    result = []
    while True:
        if does_current_window_contain_concatenation():
            result.append(start)

        if end >= len(str1):
            break

        next_snip = str1[end: end + word_length]
        if next_snip in window_info:
            window_info[next_snip] -= 1

        prev_snip = str1[start: start + word_length]
        if prev_snip in window_info:
            window_info[prev_snip] += 1

        start += word_length
        end += word_length

    return result


def driver_func(str1: str, words: List[str]) -> List[int]: # Accepted on Leetcode
    result = []
    for i in range(len(words[0])):
        result.extend(map(lambda x: x + i, find_substring(str1[i:], words)))

    return result


if __name__ == "__main__":
    print(driver_func("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]))
