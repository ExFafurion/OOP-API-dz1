
with open("recipes.txt") as f:
    for line in f:
        dish_name = line.strip()
        ingredients_qty = int(f.readline().strip())
        ingredients_list = []
        for ingredient_line in range(ingredients_qty):
            item1, item2, item3 = f.readline().split("|")
            ingredient_dict = {
                'ingredient_name': item1.strip(),
                'quantity': item2.strip(),
                'measure': item3.strip()
            }
            ingredients_list.append(ingredient_dict)
        cook_book[dish_name] = ingredients_list
print(cook_book)