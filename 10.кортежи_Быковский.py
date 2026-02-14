otveti = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)
otv = []
for i in range(len(otveti)):
    otv.append(int(input("Введите ответ ")))
if otv == list(otveti):
    print("Экзамен сдан")
else:
    print("Экзамен провален")



