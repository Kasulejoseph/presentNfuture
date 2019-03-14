def binarySearch(arrayN, x):
    for count, item in enumerate(arrayN, start=1):
        if len(arrayN) % 2 == 0:
            mid = len(arrayN) // 2
            print('fghcvgvgh', count, item, mid)
        if len(arrayN) % 2 == 1:
            mid = len(arrayN) //2
        print(count, item, mid)
        if x < arrayN[mid]:
            mid = (arrayN[mid]-1) //2
            print('iuyuyyu', mid)
        if x > arrayN[mid]:
            mid = ((len(arrayN)-1) + arrayN[mid]) //2
            print('yoooooo', mid)
        if x == arrayN[mid]:
            return x
print(binarySearch([1, 2, 3, 4, 5], 5))

