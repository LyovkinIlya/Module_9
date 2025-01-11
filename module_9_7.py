def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res > 1:
            for i in range(2, res):
                if res % i == 0:
                    print('Число составное')
                    break
            else:
                print('Число простое')
        else:
            print('Число не простое и не составное')
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)


