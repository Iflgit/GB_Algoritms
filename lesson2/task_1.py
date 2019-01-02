# 1. Написать программу, которая будет складывать, вычитать, умножать или делить
# два числа. Числа и знак операции вводятся пользователем. После выполнения
# вычисления программа не должна завершаться, а должна запрашивать новые данные
# для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции. Также сообщать пользователю
# о невозможности деления на ноль, если он ввел 0 в качестве делителя.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing

while True:
    print("Необходимо ввести 2 числа для операции")
    first = int(input("Первое число: "))
    second = int(input("Второе число: "))
    while True:
        print("Введите символ операции(+-*/) или 0 для выхода")
        sign = input("Операция: ")
        if sign == "0":
            exit(0)
        elif sign in ("+", "-", "*", "/"):
            break
        else:
            print(f"Введена ошибочная команда '{sign}'")
            continue

    if sign == "+":
        print(f"{first} + {second} = {first + second}")
    elif sign == "-":
        print(f"{first} - {second} = {first - second}")
    elif sign == "*":
        print(f"{first} * {second} = {first * second}")
    else:
        if second == 0:
            print("На ноль делить нельзя!")
        else:
            print(f"{first} / {second} = {first / second}")
