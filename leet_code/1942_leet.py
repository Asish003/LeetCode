times = [[1,4],[2,3],[4,6]]
targetFriend = 1

sorted_times = []

for i in range(len(times)):
    if times[i][1] < earliest_leave:
        earliest_leave = times[i][1]
        index = i