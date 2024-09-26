day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day <= 31):
    season = "Весна"
elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 8 and day <= 31):
    season = "Лето"
elif (month == 9 and day >= 1) or (month == 10) or (month == 11 and day <= 30):
    season = "Осень"
else:
    season = "Зима"

print(f"Дата: {day}.{month} относится к сезону: {season}")