def stack_operation(stack_commands):
    stos = []
    _max = []
    for i in stack_commands:
        if 'push' in i:
            number = i[1:]
            a = list(number)
            stos.append(a)
        if 'pop' in i:
            stos.pop()
        if 'show_max' in i:
            number = stos[-1:]
            a = list(number)
            _max.append(a)

    print(_max)
    return(_max)

commands = [
    ('push', 97),
    ('pop',),
    ('push', 20),
    ('pop',),
    ('push', 26),
    ('push', 20),
    ('pop',),
    ('show_max',),
    ('push', 91),
    ('show_max',)
]
assert stack_operation(commands) == [26, 91]
