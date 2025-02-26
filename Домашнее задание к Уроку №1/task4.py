# Создать две переменные «a» и «b» от -10 до 10. Значения вводит пользователь.
# Затем написать скрипт, который работает по следующему принципу:
# если “a” и “b” положительные, вывести их разность;
# если “a” и “b” отрицательные, вывести их произведение;
# если “a” и “b” разных знаков, вывести их сумму;


a = input()
b = input()
def error_value(name):
    print(f'Проверьте значение числа {name}')

def error_value_border(value):
    if not -10 <= int(value) <= 10:
        print(f'Число {value} не соотвутствует границам [-10; 10]')
        return False
    return True

def check_value(value):
    mid = value
    znak = ""
    if value[0] == "-":
        znak = "-"
        mid = value[1:]
    if mid.isdigit():
        if error_value_border(znak+mid):
            return True
    return False

if check_value(a):
    if check_value(b):
        a = int(a)
        b = int(b)
        if a > -1 and b > -1:
            print(a - b)
        elif a < 0 and b < 0:
            print(a*b)
        else:
            print(a+b)
    else:
        error_value('b')
else:
    error_value('a')



# Альтернативный вариант через try-except
# try:
#     if -10 <= int(a) <= 10:
#         try:
#             if -10 <= int(b) <= 10:
#                 a = int(a)
#                 b = int(b)
#                 if a > -1 and b > -1:
#                     print(a - b)
#                 elif a < 0 and b < 0:
#                     print(a*b)
#                 else:
#                     print(a+b)
#             else:
#                 print("Число \"b\" меньше -10 или больше 10. Введите значение числа заново!")
#         except ValueError:
#             print("Значение числа \"b\" введено неверно!")
#     else:
#         print("Число \"a\" меньше -10 или больше 10. Введите значение числа заново!")
# except ValueError:
#     print("Значение числа \"a\" введено неверно!")