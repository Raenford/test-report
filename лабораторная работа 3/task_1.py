# TODO Напишите функцию для поиска индекса товара
def finder():
    if find_item in items_list:
        return items_list.index(find_item)
    else:
        return None





items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finder()
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
