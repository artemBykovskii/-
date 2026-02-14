
"""import datetime
current_time = datetime.datetime.now()
print(current_time)"""



"""import random
random_list = []
random_list = str(random.randint(1,100))
randomer_numbe = random.choice(random_list)
print(randomer_numbe, random_list)"""



"""import matplotlib.pyplot as plt
import random
number_a = list(range(1,13))
number_b = random.sample(range(1000), 12)
plt.plot(number_a,number_b)
plt.show()"""



"""import random
adm_number=random.randint(1,9)
def sum_numbers(num):
    sum = 0
    num=int(num)
    while num != 0:
        sum+=num % 10
        num=num // 10
    return sum
def lottery(numbers):
    win=[]
    for number in numbers:
        if sum_numbers(number)%adm_number==0:
            win.append(number)
            if len(win) ==  5:
                break
    return win
print(adm_number)
print(lottery(list(range(100))))"""


"""import random
quantity = int(input())
while quantity > 0:
    qu = random.randint(1,2)
    if qu == 1:
        print('Орёл')
    else:
        print('Решка')
    quantity -= 1"""


"""import random
quantity = int(input())
while quantity > 0:
    qu = random.randint(1,6)
    print(qu)
    quantity -= 1"""


"""import random
quantity = int(input())
parol = ''
while quantity > 0:
    qu = random.randint(ord('A'), ord('z'))
    parol += chr(qu)
    quantity -= 1
print(parol)"""





