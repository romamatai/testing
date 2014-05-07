#!/usr/bin/env python

#
# Make a heap datastructure from a given input array
#

import math

def makeHeap(arr):
    for i in range(len(arr) - 1, -1, -1):
        parent = int(math.floor((i - 1) /2))
        while (i > 0 and arr[i] > arr[parent]):
            temp = arr[i]
            arr[i] = arr[parent]
            arr[parent] = temp
            i = parent
            parent = int(math.floor((i - 1) / 2))


a = [7, 2, 9, 10, 15, 1, 3]
print a
makeHeap(a)
print a
