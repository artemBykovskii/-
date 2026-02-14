def calculate_age(cur_year, birth_year):
    return cur_year - birth_year
my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print(f"Мне {my_age} лет, а моему отцу {dads_age}")
