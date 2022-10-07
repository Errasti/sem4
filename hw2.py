def simplify_number(n):
    i = 2
    mult_numbers = []
    while i <= n:
        while n % i == 0:
            mult_numbers.append(int(i))
            n = n / i
        i += 1
    if n > 1:
        mult_numbers.append(int(n))
    return mult_numbers


user_n = int(input("Введите N: "))
print(simplify_number(user_n))
