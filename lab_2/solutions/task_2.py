def stack_operation(stack_commands):
    """
    Funkcja przyjmuję listę jedno i dwu elementowych krotek - operacji na stosie.
    Pierwszy element krotki to operacja, drugi wartość (opcjonalnie). Operacje:
    push - dodaj element do stosu
    pop - usuń element ze stosu
    show_max - wypisz maksymalny element w stosie
    Uzupełnij funkcje tak, by dla podanej zwróciła ciąg maksymalnych elementów (zgodny z liczbą operacj 3).

    :param stack_commands: List of tuples of stack commands.
    :type stack_commands: list
    :return: List of outputs from commands.
    :rtype: list
    """
    stack = []
    max_vals = []
    for cmd in stack_commands:
        if cmd[0] =='push':
            stack.append(cmd[1])
        elif cmd[0] == 'pop':
            stack.pop()
        elif cmd[0] == 'show_max':
            max_vals.append(max(stack))

    return max_vals


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
