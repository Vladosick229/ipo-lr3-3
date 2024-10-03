day = int(input("Введите день: "))# ввод дня
month = int(input("Введите месяц: ")) # ввод месяца
if month<1 or month>12: # Проверяем на корректный месяц.

    print("Ошибка месяца") # Выводим что у нас некорректный месяц.

elif day<1 or day>31: # Проверяем на корректный день.
    
    print ("Некорректный день") # Выводим что у нас некорректный день.
    
else:# Если day и month валидны, выполниться этот блок.
if (month == 3 and day >= 1) or (month == 4) or (month == 5 and day <= 31):
    season = "Весна"
elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 8 and day <= 31):
    season = "Лето"
elif (month == 9 and day >= 1) or (month == 10) or (month == 11 and day <= 30):
    season = "Осень"
else:
    season = "Зима"

print(f"Дата: {day}.{month} относится к сезону: {season}")
