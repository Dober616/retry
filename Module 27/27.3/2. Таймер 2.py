import time


def timer_2(func):
    def wrapped_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        run_time = round(finish_time - start_time, 4)
        print(f'Функция выполнялась {run_time} секунд')
        return result
    return wrapped_func

@timer_2
def summ(number):
    my_summ = 0
    for i in range(number):
        my_summ += i ** 3
    return my_summ


print(summ(10000))
