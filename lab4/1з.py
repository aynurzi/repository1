import json


def task() -> float:
    # открываем файл
    with open('input.json', 'r') as f:
        data = json.load(f)

    # вводим ключи
    sum_of_products = 0
    for item in data:
        sum_of_products += item['score'] * item['weight']

    return round(sum_of_products, 3)


print(task())
