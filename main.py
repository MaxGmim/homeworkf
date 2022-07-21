def open_file():
    with open('recipes.txt') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            cook_book.update({line: []})
            k = int(file.readline().strip())
            for _ in range(k):
                lst = file.readline().strip().split(' | ')
                dict = {'ingredient_name': lst[0], 'quantity': lst[1], 'measure': lst[2]}
                cook_book[line].append(dict)
            file.readline()
    return cook_book



def view_cook_book():
    for key, value in open_file().items():
        print(f'\n {key}')
        for dct in value:
            print(f"    {dct['ingredient_name'] + ' - ' + dct['quantity'] + ' ' + dct['measure']}")


def view_shopping_list(s_l):
    print('\nДля приготовления этих блюд пондобится:\n')
    index = 1
    for key, values in s_l.items():
        print(f"   {index}. {key} {values['quantity']} {values['measure']}")
        index += 1


def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for ingred in dishes:
        for ingr in open_file()[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in shopping_list:
                ingr['quantity'] += shopping_list[name_ingr]['quantity']
            shopping_list.update({name_ingr: ingr})
    view_shopping_list(shopping_list)



def input_ingredients():
        lst = list(input('Введите через запятую блюда: ').split(', '))
        persons = int(input('Введите количество персон: '))
        get_shop_list_by_dishes(lst, persons)


def very_main():
    print('\n\nВведите функцию: '
          '\n\n   1. Вывод рецептов.'
          '\n   2. Ввод нужных рецептов и количества человек.')
    while True:
        prog = str(input('\n\n  номер действия: '))
        if prog == '1':
            view_cook_book()
        elif prog == '2':
            input_ingredients()
        else:
            print('\n Ошибка ')


if __name__ == '__main__':
    very_main()







