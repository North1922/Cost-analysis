import datetime
from datetime import date


records = [] #список для зранения записей представленных кортежами (название покупки,сумма,категория)
shopping_dict = {} #словарь ключ-категория: значение-список кортежей(название покупки, сумма)
count = 0
list_of_tuples = []
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
    while count < len(records):
        name, amount, category = records[count]# распаковываем кортеж элемента под номером count в списке records
        the_amount += int(amount)# в переменной the_amount суммируем все суммы покупок
        count += 1 # увеличиваем счётчик на 1
        if category in shopping_dict: #Проверяем есть ли категория в словаре
            shopping_dict[category].append((name, int(amount)))# Добавляем кортеж в список которых хранится в качестве значения
        else:
            shopping_dict[category] = [(name, int(amount))]# Если категории нет, создаем новую ячейку в качестве ключа Категория,
            # в качестве значения список который содержит в себе кортеж с name и amount



average_expense = the_amount / len(records)
print('--------------')
print(f'Кол-во покупок: {len(records)}. Общая сумма расходов: {the_amount}. '
      f'Среднее значение расходов по всем категориям: {average_expense}')
print('--------------')
list_of_keys = list(shopping_dict.keys()) # получили список с ключами
index = 0 # счётчик который будем использовать для доступа к элементам списка
# Используем цикл while для итерации по категориям
while index < len(list_of_keys):
    category = list_of_keys[index]
    purchases_list = shopping_dict[category]
    total_amount = sum(item[1] for item in purchases_list) # Вычисляем суммарную стоимость покупок в категории
    average_amount = total_amount / len(purchases_list) # средня стоимость

    # Выводим результаты
    print(f"Категория: {category}")
    print(f"Список покупок: {purchases_list}")
    print(f"Суммарная стоимость: {total_amount}")
    print(f"Средняя сумма: {average_amount}")
    print('--------------')  # Пустая строка для разделения категорий

    # Увеличиваем индекс для перехода к следующей категории
    index += 1

date_now = date.today()
time_now = datetime.datetime.now()
current_time = time_now.time().strftime('%X')
print(f"Дата: {date_now}. Время: {current_time}.")