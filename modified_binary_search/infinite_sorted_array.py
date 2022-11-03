import math

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

def search_in_infinite_array(reader, target):
    start = 0
    end = 1

    while reader.get(end) < target:
        new_start = end + 1
        end += (end - start + 1) * 2
        start = new_start

    while start <= end:
        mid = (start + end) // 2

        if reader.get(mid) == target:
            return mid
        elif reader.get(mid) < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1



if __name__ == "__main__":
    reader1 = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader1, 16))
    print(search_in_infinite_array(reader1, 11))

    reader2 = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader2, 15))
    print(search_in_infinite_array(reader2, 200))
