# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

#     год, номер которого кратен 400, — високосный;
#     остальные годы, номер которых кратен 100, — невисокосные;
#     остальные годы, номер которых кратен 4, — високосные.

print("Введите год для проверки на високосность")
year = int(input("год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}-й год високосный")
else:
    print(f"{year}-й год не високосный")
