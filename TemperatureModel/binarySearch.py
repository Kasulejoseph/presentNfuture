def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first <=last and not found:
        mid = (first + last) //2
        if item == alist[mid]:
            found = True 
        else:
            if item > mid:
                first = mid +1
            else:
                last = mid -1
    return found
print(binarySearch([1, 2, 3, 4, 5], 1))
            