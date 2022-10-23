def dutch_flag_sort(arr): # Verified on Leetcode
    index = 0
    num1 = -1
    num2 = len(arr)
    while index < len(arr) and index < num2:
        if arr[index] == 2:
            arr[index], arr[num2 - 1] = arr[num2 - 1], arr[index]
            num2 -= 1
            continue

        if arr[index] == 0:
            arr[index], arr[num1 + 1] = arr[num1 + 1], arr[index]
            num1 += 1

        index += 1





if __name__ == "__main__":
    input_arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(input_arr)
    print(input_arr)
