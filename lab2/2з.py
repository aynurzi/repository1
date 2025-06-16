import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_expenses = 0

for month in range(months):
    total_expenses += spend
    spend *= (1 + increase)

total_salary = salary * months

# подушка безопасности
money_capital = total_expenses - total_salary

if money_capital < 0:
    money_capital = 0

money_capital = math.ceil(money_capital)

print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", money_capital)
