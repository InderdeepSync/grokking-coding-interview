from typing import List


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


def find_max_cpu_load(jobs: List[Job]):
    # temp = list(zip(*map(lambda job: job[0:2], jobs)))
    start_times = sorted(jobs, key=lambda job: job.start) # Jobs list sorted by start_time
    end_times = sorted(jobs, key=lambda job: job.end) # Jobs sorted by end_time

    start = end = 0

    current_cpu_load = 0
    max_cpu_load = 0
    while start < len(start_times):
        if start_times[start].start < end_times[end].end:
            current_cpu_load += start_times[start].cpu_load
            max_cpu_load = max(max_cpu_load, current_cpu_load)

            start += 1
        else:
            current_cpu_load -= end_times[end].cpu_load
            end += 1
    return max_cpu_load



if __name__ == "__main__":
    # Job : [start_time, end_time, cpu_load]
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))
