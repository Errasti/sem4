d = float(input("Обозначьте точность d: "))
k = 1
pi = 0
acc = int(10 / d)
for k in range(1, acc):
    pi = pi+4*((-1)**(k+1))/(2*k-1)
print(f'Ответ: {str(pi)[:5]}')
