def task_1():
    a = "\n"
    for i in range(1,10):
        a = a+(str(i)*i)+"\n"
    print(a)
    return a


assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
