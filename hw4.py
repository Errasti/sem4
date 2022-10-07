from random import randint


k = int(input('Введите натуральную степень k:'))
coeffs = [randint(0, 100) for i in range(k)]+[randint(0, 100)]
print(coeffs)
equation = '+'.join([f'{(j,"")[j == 1]}x^{i}' for i, j in enumerate(coeffs) if j][::-1])
print(equation)
equation = equation.replace('x^1+', 'x+')
equation = equation.replace('x^0', '')
equation += ('', '1')[equation[-1] == '+']
equation = (equation, equation[:-2])[equation[-2:] == '^1']
equation += "=0"
print(equation)

with open('task04.txt', 'w') as data:
    data.write(equation)



