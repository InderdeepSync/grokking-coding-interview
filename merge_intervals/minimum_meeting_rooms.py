class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings):  # Very similar to Laptop Rentals Problem AlgoExpert
    temp = list(zip(*([meeting.start, meeting.end] for meeting in meetings)))
    start_times = sorted(temp[0])
    end_times = sorted(temp[1])

    start = end = 0

    min_rooms_required = 0
    rooms_currently_occupied = 0
    while start < len(start_times):
        if start_times[start] < end_times[end]:
            rooms_currently_occupied += 1
            min_rooms_required = max(min_rooms_required, rooms_currently_occupied)
            start += 1
        else:
            rooms_currently_occupied -= 1
            end += 1


    return min_rooms_required


if __name__ == "__main__":
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
