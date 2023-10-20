salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
monthsCrit = 1  # избегаем "магических" чисел
money_capital = (salary - spend) * monthsCrit
for a in range(monthsCrit, months, 1):
    spend = spend * (1 + increase)
    money_capital = money_capital + salary - spend
money_capital = round(money_capital, 2) * (-1)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
