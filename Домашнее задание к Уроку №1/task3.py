# Попросить пользователя ввести год рождения.
# Вывести информацию о его возрасте.
import datetime
year = datetime.date.today().year # нынешний год (2025)

print("Введите свой год рождения:", end=" ")
yearUser = input()
if yearUser.isdigit():
    if year-100 < int(yearUser) < year:
        print(f"Если в этом году у Вас уже был день рождение, то Ваш возраст: {year-int(yearUser)}\nЕсли в этом году у Вас ещё не было дня рождения, то Ваш возраст: {year-int(yearUser)-1}")
    elif int(yearUser) < year-100:
        print(f"Если бы человек жил вечно, то сейчас бы Ваш возраст составил бы: {year-int(yearUser)}")
    elif int(yearUser) == year:
        print(f"Вы родились в этом году!")
    else:
        print("Вы ещё не родились.")
else:
    print("Вы ввели не год рождения!")
