def get_info(str1):
    info = {}
    for ch in str1:
        if ch in info:
            info[ch] += 1
        else:
            info[ch] = 1

    return info


def checkInclusion(s1: str, s2: str) -> bool: # Accepted on Leetcode
    start = 0
    end = len(s1)

    window_info = get_info(s1)

    for ch in s2[start: end]:
        if ch in window_info:
            window_info[ch] -= 1

    def does_current_window_contain_permutation():
        for key in window_info:
            if window_info[key] > 0:
                return False

        return True

    while True:
        if does_current_window_contain_permutation():
            return True

        if end >= len(s2):
            return False
        if s2[end] in window_info:
            window_info[s2[end]] -= 1

        if s2[start] in window_info:
            window_info[s2[start]] += 1

        start += 1
        end += 1


if __name__ == "__main__":
    print(checkInclusion("ab", "a"))