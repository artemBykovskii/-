# Задача 1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
f100_to_celsius = f_to_c(100)

def c_to_f(c_temp):
    f_temp = c_temp *9/5 + 32
    return f_temp
c0_in_fahrenheit = c_to_f(0)


# Задача 2
def get_force(m, a):
    return m * a
def get_energy(m, c = 3*10**8):
    return m * c ** 2
def get_work(m, a, distance):
    f = get_force(m, a)
    return f * distance
bomb_mass = 1
train_mass = 22600
train_acceleration = 10
train_distance = 100
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print(f"Поезд GE поставляет {train_force} Ньютонов силы")
bomb_energy = get_energy(bomb_mass)
print(f"1 кг бомбы составляет {bomb_energy} Джоулей")
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров")


# Задача 3
clothes = "домашняя одежда"
def vivod(par1, par2):
    print(f"{par1} лучше всего подходит {par2}")
print("У меня большой гардероб")
times_of_day = ["Утром", "Днём", "Вечером", "Ночью"]
for i in times_of_day:
    vivod(i, clothes)
meal = ["каша", "суп", "курица"]
times_to_eat = ["На завтрак", "На обед", "На ужин"]
for i in range(len(times_to_eat)):
    vivod(times_to_eat[i], meal[i])



# Задача 4
def proverka(user_name: str, ARM: int):
    if [user_name, str(ARM)] in users:
        print(greetings)
    elif [user_name, str(ARM)] not in users and user_name != "Дмитрий":
        print("Логин или пароль не верный, попробуйте еще раз")
    elif [user_name, str(ARM)] not in users and user_name == "Дмитрий":
        print(Dmitriy_check)
users = [["Дмитрий", "1"],["Ангелина", "2"],["Василий", "3"],["Екатерина", "4"]]
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
greetings = "Добро пожаловать"
proverka("Ангелина", 3)
proverka("Екатерина", 4)
proverka("Дмитрий", 1)
proverka("Дмитрий", 2)



# Задача 5
def func(grade: float):
    if grade >= 4:
        return "A"
    elif grade >= 3:
        return "B"
    elif grade >= 2:
        return "C"
    elif grade >= 1:
        return "D"
    elif grade >= 0:
        return "F"
grade = float(input())
print(func(grade))
