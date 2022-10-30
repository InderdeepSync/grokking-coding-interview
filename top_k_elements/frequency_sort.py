
import heapq

def frequencySort(s: str) -> str: # Verified on Leetcode
    info = {}
    for ch in s:
        if ch not in info:
            info[ch] = 1
        else:
            info[ch] += 1

    min_heap = []
    for ch, freq in info.items():
        min_heap.append((freq, ch))

    heapq.heapify(min_heap)

    result = []
    while min_heap:
        freq, ch = heapq.heappop(min_heap)
        result.insert(0, ch * freq)

    return "".join(result)





if __name__ == "__main__":
    print(frequencySort("tree"))