def task_1():
    a = ''
    for iter in range(1,10):
        print(str(iter) * iter)
    	a += str(iter) * iter
    return a


assert task_1() 
