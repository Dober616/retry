import time


def my_timer(funk, *args, **kwargs):
    started_at = time.time()
    result = funk(*args, **kwargs)
    finished_at = time.time()
    run_time = round(finished_at - started_at, 4)
    print(f'Функция работала {run_time} секунд')
    return result


def number_summ(number):
    summ = 0
    for i in range(number + 1):
        summ += i ** 3
    return summ


print(my_timer(number_summ, 10000))
