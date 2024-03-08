l = [1, 4, 5, 1, 6, 1, 10]

def find_all(list, element):
    indexes = [] 
    for i, number in enumerate(list):
        if number == element:
            indexes.append(i)
    return indexes

element = int(input("Какое число ищем?: "))
indexes = find_all(l, element)
print("Число", element, "в списке встречается на строке:", indexes)