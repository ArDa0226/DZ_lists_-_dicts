#ДЗ_по_теме_списки_и_словарные_сборки
def exponential(x):
    return x ** 2

def the_odd(x):
    return x % 2


my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(exponential, filter(the_odd, my_list))
print(list(result))