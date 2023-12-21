# Определение категории числа
def describe_number(n):
    if n == 0:
        return "нулевое число"
    elif n < 0:
        if n % 2 == 0:
            return "отрицательное четное число"
        else:
            return "отрицательное нечетное число"
    else:
        if n % 2 == 0:
            return "положительное четное число"
        else:
            return "положительное нечетное число"

# Ввод пользователем числа
n = int(input("Введите целое число: "))

# Вывод описания числа
print(describe_number(n))