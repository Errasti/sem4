user_lst = list(map(int, input('Введите последовательность чисел:').split()))
result_lst = []
trash_lst = []
for i in range(len(user_lst)):
    temp = user_lst.pop(0)
    if temp in user_lst:
        trash_lst.append(temp)
    elif temp in trash_lst:
        trash_lst.append(temp)
    else:
        result_lst.append(temp)

print(result_lst)
