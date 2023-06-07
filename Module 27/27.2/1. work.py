import time


def timer(funk, *args, **kwargs):
    started_at = time.time()
    result = funk(*args, **kwargs)
    ended_at = time.time()
    run_time = ended_at - started_at
    print(f'Программа работала {round(run_time, 4)} сек.')
    return result


def squares_sum():
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([numm ** 2 for numm in range(10000)])
    return result


def qubes_sum(number):
    result = 0
    for _ in range(number + 1):
        result += sum([numm ** 3 for numm in range(10000)])
    return result



print(timer(squares_sum))
print(timer(qubes_sum, 200))
