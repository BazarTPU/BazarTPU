
# Ввести число и проверить, что оно является четным.
# Если четное необходимо вывести True, а иначе False
print("Введите число:", end=" ")
value = input()
if(value[0] == "-"):
    value = value[1:]
if value.isdigit():
    if int(value) % 2 == 0:
        print("True")
    else:
        print("False")
else:
    print("Вы ввели не число!")
