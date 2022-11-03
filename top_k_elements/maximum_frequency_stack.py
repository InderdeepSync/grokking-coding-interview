
import heapq


class MaxHeap:

    # Initialize the max heap
    def __init__(self, data=None):
        self.data = []

    # Push item onto max heap, maintaining the heap invariant
    def push(self, item):
        freq, order, num = item
        heapq.heappush(self.data, (-1 * freq, -1 * order, num))

    # Pop the largest item off the max heap, maintaining the heap invariant
    def pop(self):
        freq, order, num = heapq.heappop(self.data)
        return (-1 * freq, -1 * order, num)

    def __bool__(self):
        return not not self.data


class FreqStack: # Verified on Leetcode
    def __init__(self):
        self.info = {}
        self.max_heap = MaxHeap()
        self.order = 0

    def push(self, val: int) -> None:
        if val not in self.info:
            self.info[val] = 1
        else:
            self.info[val] += 1

        self.max_heap.push((self.info[val], self.order, val))
        self.order += 1

    def pop(self) -> int:
        freq, _, num = self.max_heap.pop()
        if freq > 1:
            self.info[num] -= 1
        else:
            del self.info[num]
        return num


if __name__ == "__main__":
    freqStack = FreqStack()
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)

    freqStack.pop()
    freqStack.pop()
    freqStack.pop()
    freqStack.pop()

