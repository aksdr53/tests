def integer_log(n):
    x = 0
    log = 1
    while log < n:
        log *= 2
        x += 1
    return x


print(integer_log(10))