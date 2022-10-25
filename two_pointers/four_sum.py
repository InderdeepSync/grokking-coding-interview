def search_quadruplets(arr, target):
    cache = {}
    quadruplets = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            remainder = target - (arr[i] + arr[j])
            if remainder in cache:
                quadruplets.extend([[*pair, arr[i], arr[j]] for pair in cache[remainder]])

        for k in range(i):
            pair_sum = arr[k] + arr[i]
            new_pair = [arr[k], arr[i]]
            if pair_sum not in cache:
                cache[pair_sum] = [new_pair]
            else:
                cache[pair_sum].append(new_pair)


    return quadruplets


if __name__ == "__main__":
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
