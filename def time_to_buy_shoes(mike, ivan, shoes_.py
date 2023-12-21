# Размеры инвестиций Майкла и Ивана
michael_investment = 17 # A долларов
ivan_investment = 60 # B долларов

# Минимальная сумма инвестиций
minimum_investment = 45 # X долларов

# Определение, кто из инвесторов может вложиться в стартап
michael_can_invest = michael_investment >= minimum_investment
ivan_can_invest = ivan_investment >= minimum_investment

# Вывод результата
if michael_can_invest and ivan_can_invest:
    print(2) # 2 инвестора могут вложиться
elif michael_can_invest:
    print("Mike") # Только Майкл может вложиться
elif ivan_can_invest:
    print("Ivan") # Только Иван может вложиться
elif michael_investment + ivan_investment >= minimum_investment:
    print(1) # Их сумма инвестиций равна минимальной сумме инвестиций
else:
    print(0) # Никто из инвесторов не может вложиться