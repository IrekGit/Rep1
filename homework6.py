#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
my_dict = {"Андрей": 1996, "Богдан": 2000, "Вадим": 2004, "Георгий": 2006}

#   - Выведите на экран словарь my_dict.
print(my_dict)

#   - Выведите на экран одно значение по существующему ключу,
#   одно по отсутствующему из словаря my_dict без ошибки
print("Ниже приведен список с именами учащихся:")
print(list(my_dict))
name_key_on = input("Введите имя учащегося, год рождения которого Вы хотите узнать: ")
print("Имя: " + name_key_on + ",", "год рождения: " + str(my_dict.get(name_key_on)))
name_key_off = input("Введите имя учащегося, отсутствующего в списке: ")
print("Имя: " + name_key_off + ",", "год рождения: " + str(my_dict.get(name_key_off, "Неизвестен, учащийся с таким именем отсутствует в списке")))

#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
new_name_key_1 = input("Для добавления в список введите имя нового учащегося: ")
my_dict[new_name_key_1] = int(input("Введите год рождения нового учащегося: "))
new_name_key_2 = input("Добавим в список еще одного нового учащегося с именем: ")
my_dict[new_name_key_2] = int(input("И введем его год рождения: "))
print("Ниже приведен обновленный список учащихся:")
print(my_dict)

#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.
name_del = input("Введите имя учащегося, исключаемого из списка: ")
print("Его год рождения: " + str(my_dict.pop(name_del)))
print("Список без исключенного учащегося:")
print(my_dict)

#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.
print("Работа с множеством")
my_set = {3, 5, 7, 99, 3, 5, 7, 9, True, False, (3, 0), 1, 0, 'string'}
print(my_set)
my_set.add(int(input("Введите новый элемент множества с типом int: ")))
my_set.add(str(input("Введите новый элемент множества с типом str: ")))
my_set.discard(3)
print("Получите новое множество с удаленным элеметом цифрой 3:")
print(my_set)