def stack_operation(stack_commands):
    tab_pom = []
    for val in stack_commands:
        if val[0] is 'pop':
            print("ROBIE POP")
            tab_pom.pop()
        elif val[0] is 'push':
            print("ROBIĘ PUSH")
            tab_pom.append(val[1])
        elif val[0] is 'show_max':
            print(f'max:{max(tab_pom)}')
    print(tab_pom)
    return tab_pom


if __name__ == "__main__":
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
