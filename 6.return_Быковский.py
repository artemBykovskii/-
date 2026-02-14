def calculate_age(cur_year, birth_year):
    return cur_year - birth_year
my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print(f"Мне {my_age} лет, а моему отцу {dads_age}")




def get_boundaries(target: int, margin: int):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)
print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")





def repeat_stuff(stuff: str, num_repeats = 10):
    return stuff * num_repeats
lyrics = repeat_stuff("Row", 3) + "Your Boat"
song = repeat_stuff("Stuff")
print(song)
print(lyrics)
