money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0

current_budget = money_capital + salary

while current_budget >= spend:
    # увеличиваем счетчик месяцев
    months += 1

    # начиная со второго месяца
    if months > 1:
        spend *= (1 + increase)

    current_budget = current_budget - spend + salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
