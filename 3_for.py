"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main(phone_solds):
    sold_sum = 0
    for sold in phone_solds:
        sold_sum += sold
    return round(sold_sum / len(phone_solds), 2), round(sold_sum, 2)

sum_sold_avg = 0 
all_sum = 0       
for phone in phones:
    sold_avg, sold_one = main(phone['items_sold'])
    print(f"Среднее колличество продаж {phone['product']} = {sold_avg}, сумма продаж {phone['product']} = {sold_one}")
    sum_sold_avg += sold_avg  
    all_sum += sold_one

     
         
all_avg = sum_sold_avg / len(phones)  
print('Среднее количество продаж всех товаров: ', all_avg)
print('Суммарное количество продаж всех товаров: ', all_sum)      
    
    
#if __name__ == "__main__":
#    main(phone_solds = '0')   посмотри в 5 
