money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 1
Critical = 1  # Месяц, после которого идет +%
debt = 0
while True:
    CritDamage = spend - money_capital
    if spend > salary and CritDamage > 0:
        debt = money_capital * (-1)
        break
    elif month > Critical:
        spend = spend * (1 + increase)
        money_capital += salary - spend
        month += 1
    else:
        month += 1
        money_capital += salary - spend
print("Количество месяцев, которое можно протянуть без долгов:", month)
