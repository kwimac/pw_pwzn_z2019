def counting_sort(values, _max, _min=0):
    a = range(_min, _max)
    i = _min
    sort = []
    for i in a:
        b = values.count(i)
        if b > 0:
            ii = 1
            while ii <= b:
                sort.append(i)
                ii += 1
        i +=1

    print(sort)
    return(sort)

assert counting_sort(
    [99, 4, 33, 2, 2, 1, 65, 3, 97, 53],
    100,
) == [1, 2, 2, 3, 4, 33, 53, 65, 97, 99]
