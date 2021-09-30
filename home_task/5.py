lst = list()
x = input()
while x != 'End':
    x = int(x)
    lst.append(x)
    x = input()
a = 16
try:
    for el in lst:
        print(a/el)
except ZeroDivisionError:
    print('Деление на ноль невозможно')
else:
    print('OK')
finally:
    print('Выполнение завершено')


