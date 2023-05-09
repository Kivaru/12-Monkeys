import random
import time
#naive search: scan entire list and scan if it is equal to the target, if yes return the index of no return -1
def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

#binary search uses divide and conquer on sorted list

def binary_search(list, target, low=None, high=None):

    if low is None:
        low=0
    if high is None:
        high=len(list) - 1
    if high < low:
        return -1
    
    middlepoint = (low + high) // 2

    if list[middlepoint] == target:
        return middlepoint
    elif target < list[middlepoint]:
        return binary_search(list, target, low, high=middlepoint-1)
    else:
        #target > list[middlepoint]
        return binary_search(list, target, middlepoint+1, high)

if __name__ == '__main__':
    # list = [1, 3, 5, 10, 12, 15, 30]
    # target = 15
    # print(naive_search(list, target))
    # print(binary_search(list, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end-start)/length, "seconds")