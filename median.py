from __future__ import division
def median(lst):
    lst = sorted(lst)
    lng = len(lst)
    if lng % 2 == 0:
        mid1 = int(lng / 2)
        mid2 = int((lng / 2) - 1)
        return (lst[mid1] + lst[mid2]) / 2.0
    else:
        r = int(len(lst) / 2)
        return lst[r]
