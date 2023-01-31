a = int(input('Введите 3 числа:'))
a4, a = a % 10, a // 10
a3, a = a % 10, a // 10
a2, a = a % 10, a // 10
print(a2 + a3 + a4)
print(a2 * a3 * a4)


x = int(input('Зарплата за месяц:'))
y = int(input('Платеж по кредиту в банк:'))
z = int(input('Задолженность за коммунальные услуги:'))
suma = x - (y + z)
print('Остаток свободных средств до конца месяца: ' + str(suma) + ' руб')


a = int(input("Введите дилнну первой диагонали: "))
b = int(input("Введите дилнну второй диагонали: "))
c = (a + b) * 2
print('Площадь ромба: ' + str(c))


print('To be \nor not \nto be')


print("""    «Life is what happens
    when
        you\'re busy making other plans"
                                    John Lennon.""")


