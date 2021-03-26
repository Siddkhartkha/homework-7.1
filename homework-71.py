from pprint import pprint

def read_cookbook():
    cook_dict = dict()
    with open('cook_book.txt', 'r', encoding='UTF8') as f:
        for line in f:
            dish_name = line.strip()
            ingredient_count = int(f.readline().strip())
            ingredient_list = list()
            for item in range(ingredient_count):
                ingredients = {}
                ingredient = f.readline().strip()
                ingredients['ingredient_name'], ingredients['quality'], ingredients['measure'] = ingredient.split('|')
                ingredients['quality'] = int(ingredients['quality'])
                ingredient_list.append(ingredients)
            f.readline()
            cook_dict[dish_name] = ingredient_list
        return cook_dict

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = dict()
    for dish_name in dishes:
        if dish_name in cookbook:
            for ingredients in cookbook[dish_name]:
                dinner_list = dict()
                if ingredients['ingredient_name'] not in ingredient_list:
                    dinner_list['measure'] = ingredients['measure']
                    dinner_list['quality'] = ingredients['quality'] * person_count
                    ingredient_list[ingredients['ingredient_name']] = dinner_list
                else:
                    ingredient_list[ingredients['ingredient_name']]['quality'] = \
                        ingredient_list[ingredients['ingredient_name']]['quality'] \
                        + ingredients['quality'] * person_count
        else:
            print(f'Блюда {dish_name} в списке нет\n')
    return ingredient_list

if __name__ == '__main__':
    filename = "cook_book.txt"
    cookbook = read_cookbook()
    print('Словарь из преобразованного рецепта:\n')
    pprint(cookbook)
    print(f'\nСписок игредиентов для заказанных блюд:\n')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))
