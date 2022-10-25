def interval_intersection(first_list, second_list):  # verified on leetcode
    l1 = l2 = 0

    intersection = []
    while l1 < len(first_list) and l2 < len(second_list):
        if first_list[l1][0] <= second_list[l2][1] and first_list[l1][1] >= second_list[l2][0]:
            # there is an intersection
            intersection.append([max(first_list[l1][0], second_list[l2][0]),
                                 min(first_list[l1][1], second_list[l2][1])])

        # 💡 We compare the endTimes of intervals of each list
        if first_list[l1][1] <= second_list[l2][1]:
            l1 += 1
        else:
            l2 += 1

    return intersection


if __name__ == "__main__":
    firstList = [[3, 5], [9, 20]]
    secondList = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
    print(interval_intersection(firstList, secondList))
