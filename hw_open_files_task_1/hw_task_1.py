from pprint import pprint
cook_book = {}
with open('recipes.txt', 'rt') as file:
    for l in file:
        dish_name = l.strip() #название блюда
        num_ingredients = file.readline() #количество игргидиентов
        for i in range(int(num_ingredients)):
            ingredients = file.readline() #перебор ингридиентов в строке
            ingredient_name, quantity, measure = ingredients.strip().split(' | ')
            cook_book.setdefault(dish_name, []).append({'ingredient_name': ingredient_name,
                                     'quantity' : quantity,
                                     'measure' : measure})
        blank_line = file.readline()

for key, value in cook_book.items():
    print("{0}: {1}".format(key,value))

def get_shop_list_by_dishes(dishes, person_count):
    recipes = {}
    for cook in dishes:
        for dish, sources in cook_book.items():
            if cook == dish:
                for ing in sources:
                    name = ing['ingredient_name']
                    recipes[name] = {'measure': ing['measure'],
                                     'quantities': int(ing['quantity']) * person_count}
    return recipes

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
