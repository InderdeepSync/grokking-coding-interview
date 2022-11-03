
def get_info(str1):
    info = {}
    for ch in str1:
        if ch in info:
            info[ch] += 1
        else:
            info[ch] = 1

    return info


def minWindow(s2: str, s1: str) -> str: # Accepted on Leetcode
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

    result = ""
    while start <= end:
        if does_current_window_contain_permutation():
            if not result:
                result = s2[start: end]
            else:
                result = min(result, s2[start: end], key=len)

            if s2[start] in window_info:
                window_info[s2[start]] += 1

            start += 1
        else:
            if end >= len(s2):
                break
            if s2[end] in window_info:
                window_info[s2[end]] -= 1

            end += 1

    return result


if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))
