def counting_sort(values, _max, _min=0):
    tab_pom = []
    print("Tworzenie tablicy pomocniczej")
    for i in range(_min, _max):
        tab_pom.append(0)

    print("Zliczanie poszczegolnych elementow")
    for i in values:
        print("Zliczono element: " + str(i))
        tab_pom[i] = tab_pom[i] + 1

    print("Ukladanie posortowanej tablicy")
    k = 0  # index tablicy
    for a in range(_min, _max):
        for c in range(0, tab_pom[a]):
            values[k] = a
            k = k + 1

    print(f'max:{max(values)}')
    print(f'min:{min(values)}')
    print(f'check if sorted:{values}')
    return values

if __name__ == '__main__':
    assert counting_sort(
        [99, 4, 33, 2, 2, 1, 65, 3, 97, 53],
        100,
    ) == [1, 2, 2, 3, 4, 33, 53, 65, 97, 99]
