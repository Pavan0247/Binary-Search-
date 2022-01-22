import random as r
import time as t

    # Implementation of Binary search algorithm
    # To prove Binary search is faster than the linear search
    # linear search: scan the entire list and ask if it is equal to target
    # If yes, return the index
    # If no, then return False


def linear_search(l, target):

    for i in range(len(l)):
        if l[i] == target:
            return i
    return False

    # Binary search is based on the divide and conquer rule
    # Implementaion is below

p = -1
def binary_search(l, target):
    z = 0
    u = len(l) - 1
    while z <= u:
        m = (z + u)//2
        if l[m] == target:
            globals()['p'] = m
            return True
        else:
            if l[m] < target:
                z = m+1
            else:
                u = m-1

if __name__ == '__main__':
    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(r.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    initial = t.time()
    for target in sorted_list:
        linear_search(sorted_list, target)
    end = t.time()
    print("Naive search time in seconds: ", (end - initial))

    initial = t.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = t.time()
    print("Binary search time in seconds: ", (end - initial))
