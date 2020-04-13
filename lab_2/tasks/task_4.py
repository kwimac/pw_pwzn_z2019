def count_letters(msg):
    tab_dict = {}
    for letter in msg:
        if tab_dict.get(letter):
            tab_dict[letter] = tab_dict[letter] + 1
        else:
            tab_dict[letter] = 1
        print("Zliczono literę: " + str(letter))
    print(tab_dict)
    letter_max = max(tab_dict.values())
    print(letter_max)
    list_of_chars = [key for key in tab_dict.keys() if tab_dict[key] == letter_max]
    print(list_of_chars)
    result = min(list_of_chars)
    tab_dict_2 = [result, tab_dict[result]]
    print(tab_dict_2)
    return tab_dict_2


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ['a', 4]
    assert count_letters('za') == ['a', 1]
