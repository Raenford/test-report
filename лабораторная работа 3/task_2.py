# TODO Напишите функцию find_common_participants
def find_common_participants(one, two, res=","):
    ones = one.split(res)
    twos = two.split(res)
    nonono = list(set(ones).intersection(set(twos)))
    nonono.sort()
    return nonono

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, res=","))

# TODO Провеьте работу функции с разделителем отличным от запятой
