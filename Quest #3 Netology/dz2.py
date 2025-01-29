from dz15.py import cook_book

def get_shop_list_by_dishes(dish_list, person_count):
    shop_list = {}  # Создаем пустой словарь для списка покупок

    for dish in dish_list:  # Обрабатываем каждое блюдо из списка
        if dish in cook_book:  # Проверяем наличие блюда в cook_book
            ingredients = cook_book[dish]  # Получаем список ингредиентов для блюда
            for ingredient in ingredients:  # Обрабатываем каждый ингредиент
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count  # Рассчитываем общее количество
                measure = ingredient['measure']

                if ingredient_name in shop_list:  # Если ингредиент уже есть в shop_list
                    shop_list[ingredient_name]['quantity'] += quantity  # Увеличиваем количество
                else:  # Если ингредиента нет в shop_list
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}  # Добавляем ингредиент

        else:  # Если блюда нет в cook_book
            print(f"Предупреждение: Блюдо '{dish}' отсутствует в кулинарной книге.")

    return shop_list  # Возвращаем итоговый список покупок