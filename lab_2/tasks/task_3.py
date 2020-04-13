def unique(values):
    tab_dict = {}
    for value in values:
        tab_dict[value] = 1
    print(tab_dict)
    return [*tab_dict]


if __name__ == "__main__":
    assert [1, 5, 3, 6, 7, 2, 4] == unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5])
