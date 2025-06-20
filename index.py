# Завдання 1: Користувач вводить з клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, то на екрані напис понеділок, 2 — вівторок тощо.
day = int(input("Введіть номер дня тижня (1-7): "))
if day == 1:
    print("Понеділок")
elif day == 2:
    print("Вівторок")
elif day == 3:
    print("Середа")
elif day == 4:
    print("Четвер")
elif day == 5:
    print("П’ятниця")
elif day == 6:
    print("Субота")
elif day == 7:
    print("Неділя")
else:
    print("Невірний номер дня")

# Завдання 2: Користувач вводить із клавіатури номер місяця (1-12). Необхідно вивести на екран назву місяця. Наприклад, якщо 1, то на екрані напис січень, 2 — лютий тощо.
month = int(input("\nВведіть номер місяця (1-12): "))
if month == 1:
    print("Січень")
elif month == 2:
    print("Лютий")
elif month == 3:
    print("Березень")
elif month == 4:
    print("Квітень")
elif month == 5:
    print("Травень")
elif month == 6:
    print("Червень")
elif month == 7:
    print("Липень")
elif month == 8:
    print("Серпень")
elif month == 9:
    print("Вересень")
elif month == 10:
    print("Жовтень")
elif month == 11:
    print("Листопад")
elif month == 12:
    print("Грудень")
else:
    print("Невірний номер місяця")

# Завдання 3:Користувач вводить суму покупки і свій вік. Програма обчислює знижку
# Якщо вік менше 18, знижка 10%.
# Від 18 до 60 років — знижка 5%.
# Якщо вік більше 60 років — знижка 15%. Програма виводить підсумкову суму з урахуванням знижки.
summa = float(input("\nВведіть суму покупки: "))
age = int(input("Введіть ваш вік: "))
if age < 18:
    discount = 0.10
elif age <= 60:
    discount = 0.05
else:
    discount = 0.15
final_sum = summa * (1 - discount)
print(f"Сума до оплати зі знижкою: {round(final_sum, 2)} грн")

# Завдання 4: Користувач вводить оцінки з трьох предметів (від 1 до 5). Програма перевіряє, чи є серед них хоча б одна "двійка". Якщо так, виводиться повідомлення "Незадовільно". Якщо всі оцінки 4 і вище, виводиться "Відмінно".
g1 = int(input("\nВведіть оцінку з першого предмету (1-5): "))
g2 = int(input("Введіть оцінку з другого предмету (1-5): "))
g3 = int(input("Введіть оцінку з третього предмету (1-5): "))

if g1 == 2 or g2 == 2 or g3 == 2:
    print("Незадовільно")
elif g1 >= 4 and g2 >= 4 and g3 >= 4:
    print("Відмінно")
else:
    print("Задовільно")

# Завдання 5: Користувач вводить оцінки з чотирьох предметів (від 1 до 5). Програма перевіряє, чи може він бути допущений до іспиту:
# Якщо хоча б одна оцінка нижче 3, студент не допускається до іспиту.
# Якщо всі оцінки 4 і вище, студент допускається до іспиту з відзнакою.
# У всіх інших випадках студент допускається до іспиту.
e1 = int(input("\nОцінка з 1-го предмета(1-5): "))
e2 = int(input("Оцінка з 2-го предмета(1-5): "))
e3 = int(input("Оцінка з 3-го предмета(1-5): "))
e4 = int(input("Оцінка з 4-го предмета(1-5): "))

if e1 < 3 or e2 < 3 or e3 < 3 or e4 < 3:
    print("Студент не допускається до іспиту")
elif e1 >= 4 and e2 >= 4 and e3 >= 4 and e4 >= 4:
    print("Студент допускається до іспиту з відзнакою")
else:
    print("Студент допускається до іспиту")
# Завдання 6: Користувач вводить дані про свій автомобіль: вік і пробіг. Програма виводить рекомендацію:
# Якщо вік автомобіля менше 3 років і пробіг до 30000 км — "Автомобіль у відмінному стані".
# Якщо вік до 10 років і пробіг до 100000 км — "Автомобіль у хорошому стані".
# В інших випадках — "Автомобіль потребує перевірки".
car_age = int(input("\nВведіть вік автомобіля (у роках): "))
car_mileage = int(input("Введіть пробіг автомобіля (у км): "))

if car_age < 3 and car_mileage <= 30000:
    print("Автомобіль у відмінному стані")
elif car_age <= 10 and car_mileage <= 100000:
    print("Автомобіль у хорошому стані")
else:
    print("Автомобіль потребує перевірки")

