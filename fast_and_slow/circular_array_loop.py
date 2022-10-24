def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        direction = 1 if arr[i] > 0 else -1
        slow = fast = i

        while arr[fast] * direction > 0 and (arr[(fast + arr[fast]) % len(arr)]) * direction > 0:
            slow = (slow + arr[slow]) % len(arr)
            fast = (fast + arr[fast]) % len(arr)
            fast = (fast + arr[fast]) % len(arr)

            if fast == slow:
                if arr[fast] % len(arr) != 0:
                    return True
                break

    return False


if __name__ == "__main__":
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, -1, 1, -2, -2]))
