
import heapq


def reorganizeString(s: str) -> str: # Verified on Leetcode
    info = {}
    for ch in s:
        if ch not in info:
            info[ch] = 1
        else:
            info[ch] += 1

    max_heap = []

    for ch, freq in info.items():
        heapq.heappush(max_heap, (-freq, ch))

    result = ""
    while max_heap:
        temp_arr = []
        temp = 0
        while max_heap and temp < 2:
            freq, ch = heapq.heappop(max_heap)
            freq = -1 * freq
            if result and result[-(2 - 1):].count(ch) > 0:
                return ""
            result = result + ch
            if freq > 1:
                temp_arr.append((-1 * (freq - 1), ch))

            temp += 1

        while temp_arr:
            heapq.heappush(max_heap, temp_arr.pop())

    return result


if __name__ == "__main__":
    print(reorganizeString("vvvlo"))