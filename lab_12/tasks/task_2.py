from datetime import datetime
from functools import wraps
import time


def log_run(fun):



    def wrapper(*args, **kwargs):
        print(datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
        print(f'{len(args)} positional parameters')
        for k, v in kwargs.items():
            print(f'optional parameters: {k}')
        if not kwargs:
            print("optional parameters: -")
        start = time.perf_counter()
        to_return = fun(args[0])
        stop = time.perf_counter()
        print(f'returned: {to_return} ({(stop-start):.2e}s)')

        return to_return

    return wrapper



@log_run
def fun(*args, **kwargs):
    pass


if __name__ == '__main__':
    decorated_sum = log_run(sum)
    decorated_sum([1,2,3])
    fun(1, 2, 'a', bb=1)
    # Przykładowy log
    # 2020-01-23T21:09:55| function sum called with:
    # 1 postional parameters
    # optional parameters: -
    # returned: 6 (1.43e-06s)
    # 2020-01-23T21:09:55| function fun called with:
    # 3 postional parameters
    # optional parameters: bb
    # returned: None (1.43e-06s)
