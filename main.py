import datetime
from datetime import date


records = [] #список для зранения записей представленных кортежами (название покупки , сумма, категория)
shopping_dict = {} #словарь ключ-категория: значение-список кортежей(название покупки, сумма)
the_amount = 0 # сумма расходов
average_expense = 0# средние расходы
while True:
    purchases = input('Введите покупки в формате: название покупки:сумма:категория. '
                      '"Стоп" для завершения ввода.').lower()
    if purchases == 'стоп':
        break

    parts = purchases.split(':')

    if len(parts) != 3 or not purchases.split(':')[1].isdigit():
        print('Некорректный формат ввода')
        continue

    records.append(tuple(parts))# преобразовали полученную строку parts в кортеж и добавили в список records, что бы
    # далее циклом пройтись по списку и делать необходимые действия с данными
    # print(records)
    # нужен цикл который бежит по списку и работает с кортежами внутри списка

    name, amount, category = parts
    the_amount += int(amount) #считаем общую стоимость покупок

    if category in shopping_dict:
        shopping_dict[category].append((name, int(amount)))
    else:
        shopping_dict[category] = [(name, int(amount))]


average_expense = the_amount / len(records)
print('--------------------------')
print(f'Кол-во покупок: {len(records)}. Общая сумма расходов: {the_amount}. '
      f'Среднее значение расходов по всем категориям: {average_expense}')
print('--------------------------')
list_of_keys = list(shopping_dict.keys()) # получили список с ключами
index = 0 # счётчик, который будем использовать для доступа к элементам списка
# Используем цикл while для итерации по категориям
while index < len(list_of_keys):
    category = list_of_keys[index] # в переменную category помешаем наименование категории , посредством обращения к
    # элементу списка в котором хранятся все ключи (категории)
    purchases_list = shopping_dict[category] # в переменную помещаем список всех покупок из категории
    total_amount = sum(item[1] for item in purchases_list) # Вычисляем суммарную стоимость покупок в категории
    average_amount = total_amount / len(purchases_list) # средня стоимость
    purchases_str = ""
    i = 0
    while i < len(purchases_list):
        item = purchases_list[i]
        purchases_str += f"{item[0]}"
        if i < len(purchases_list) - 1:
            purchases_str += ", "
        i += 1
    # Выводим результаты
    print(f"Категория: {category}")
    print(f"Список покупок: {purchases_str}")
    print(f"Суммарная стоимость: {total_amount}")
    print(f"Средняя сумма: {average_amount}")
    print('--------------------------')  # Пустая строка для разделения категорий

    # Увеличиваем индекс для перехода к следующей категории
    index += 1

date_now = date.today() #обращаемся к date при помощи метода today() который аозвращает нам текущую дату
time_now = datetime.datetime.now() #для получения времени, сначала необходимо получить дату и время,
# а затем достать из этого объекта только время с помощью метода time():
current_time = time_now.time().strftime('%X') #достаём из time_now время при помощи .time() и форматируем при помощи
# strftime('%X') в локальную версию времени
print(f"Дата: {date_now}. Время: {current_time}.")
