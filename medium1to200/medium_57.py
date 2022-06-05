class Solution:
    def insert(self, intervals, newInterval):
        s = newInterval[0]
        e = newInterval[1]
        left = []
        right = []
        for i in intervals:
            # add to list if no overlapping
            if s>i[1]:
                left += [i]
            elif e<i[0]:
                right += [i]
            # there is overlapping, merge current range
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        print(left, right)
        return left + [[s, e]] + right
