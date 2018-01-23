def mergeIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda tup: tup[0])
    mergedIntervals = []

    for t in sortedIntervals:
        if not mergedIntervals:
            mergedIntervals.append(t)
        else:
            p = mergedIntervals.pop()
            if p[1] >= tup[0]:
                new_t = tuple([p[0], tup[1]])
                mergedIntervals.append(new_t)
            else:
                mergedIntervals.append(p)
                mergedIntervals.append(tup)
    return mergedIntervals

intervals = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]

print mergeIntervals(intervals)