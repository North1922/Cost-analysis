import datetime
import colorama

from colorama import Fore, Back, Style
from datetime import date

colorama.init()# инициализируем colorama перед использованием
records = [] #список для зранения записей представленных кортежами (название покупки , сумма, категория)
shopping_dict = {} #словарь ключ-категория: значение-список кортежей(название покупки, сумма)
the_amount = 0 # сумма расходов
average_expense = 0# средние расходы
while True:
    purchases = input(Fore.GREEN + 'Введите покупки в формате:'+ Style.RESET_ALL + ' название покупки:сумма:категория. ' +
                      Fore.BLUE + Style.BRIGHT +'Стоп'+ Style.RESET_ALL + ' для завершения ввода.').lower()
    if purchases == 'стоп':
        break

    parts = purchases.split(':')

    if len(parts) != 3 or not purchases.split(':')[1].isdigit():
        print(Fore.RED + Style.BRIGHT + 'Некорректный формат ввода' + Style.RESET_ALL)
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
print(Fore.RED + '--------------------------' + Style.RESET_ALL)
print(Fore.CYAN + f' Кол-во покупок:{Style.RESET_ALL} {len(records)} ||' +
      Fore.CYAN + f' Общая сумма расходов:{Style.RESET_ALL} {the_amount} ||' +
      Fore.CYAN + f' Среднее значение расходов по всем категориям:{Style.RESET_ALL} {int(average_expense)} ||')
print(Fore.RED + '--------------------------' + Style.RESET_ALL)
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
    print(Fore.YELLOW + "Категория покупок: " + Style.RESET_ALL + category)
    print(Fore.YELLOW + "Список покупок: " + Style.RESET_ALL + purchases_str)
    print(Fore.YELLOW + "Суммарная стоимость: " + Style.RESET_ALL + str(total_amount))
    print(Fore.YELLOW + "Средняя сумма: " + Style.RESET_ALL + str(average_amount))
    print(Fore.RED + '--------------------------' + Style.RESET_ALL)  # Пустая строка для разделения категорий

    # Увеличиваем индекс для перехода к следующей категории
    index += 1

date_now = date.today() #обращаемся к date при помощи метода today() который аозвращает нам текущую дату
time_now = datetime.datetime.now() #для получения времени, сначала необходимо получить дату и время,
# а затем достать из этого объекта только время с помощью метода time():
current_time = time_now.time().strftime('%X') #достаём из time_now время при помощи .time() и форматируем при помощи
# strftime('%X') в локальную версию времени
print(f"{Fore.MAGENTA}Дата:{Style.RESET_ALL} {date_now}. {Fore.MAGENTA}Время:{Style.RESET_ALL} {current_time}.")
