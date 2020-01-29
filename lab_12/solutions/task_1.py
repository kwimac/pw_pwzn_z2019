def generate_fibonacci(n=100):
    try:
        n = int(n)
    except ValueError:
        raise RuntimeError('Błędna liczba kroków')
    if n < 1 or n > 100:
        raise RuntimeError('Błędna liczba kroków')

    a = 0
    yield a
    step = 1

    b = 1
    while step < n:
        yield b
        tmp = a + b
        a = b
        b = tmp
        step += 1


if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)
