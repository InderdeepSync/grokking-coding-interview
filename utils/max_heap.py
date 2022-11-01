import heapq

class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    def push(self, item):
        if isinstance(item, tuple):
            item = (-1 * item[0], item[1])
        else:
            item = -1 * item
        heapq.heappush(self.data, item)

    # Pop the largest item off the max heap, maintaining the heap invariant
    def pop(self):
        item = heapq.heappop(self.data)
        if isinstance(item, tuple):
            return -1 * item[0], item[1]
        else:
            return -1 * item

    # Pop and return the current largest value, and add the new item
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)

    # Return the current largest value in the max heap
    def top(self):
        item = self.data[0]
        if not isinstance(item, tuple):
            return -1 * item

        return -1 * item[0], item[1]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def __bool__(self):
        return bool(self.data)