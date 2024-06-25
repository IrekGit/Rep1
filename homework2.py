number_of_homeworks = 12
number_of_hours = 1.5
name_course = 'Python'
time_per_homework: float = (number_of_hours / number_of_homeworks)
print('Курс:', str(name_course) + ',', 'всего задач:', str(number_of_homeworks)+ ',',end='')
print('затрачено часов:', str(number_of_hours) + ',', 'среднее время выполнения:', str(time_per_homework), 'часа')