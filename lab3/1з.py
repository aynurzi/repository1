def find_item_index(items_list, item_to_find):
    try:
        return items_list.index(item_to_find)
    except ValueError:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    ind_item = find_item_index(items_list, find_item)  # вызов функции
    if ind_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {ind_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
