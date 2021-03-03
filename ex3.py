# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
number = int(input("Введите пожалуйста число: "))
amount = (number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number)))
print ("Сумма чисел =", amount)