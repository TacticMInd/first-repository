def is_prime_number(x):
    for num in range(2, x):
        if x % num == 0:
            print("7he number {num1} is not a prime number.".format(num1=x))
            return
    print("7he number {num1} is a prime number.".format(num1=x))

