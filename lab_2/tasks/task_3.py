def unique(values):
    list = []
    for i in values:
        a = values.count(i)
        if a == 1:
            list.append(i)
        else:
            if i in list:
                None
            else:
                list.append(i)
        i += 1

    print(list)
    return(list)

assert [1, 5, 3, 6, 7, 2, 4] == unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5])