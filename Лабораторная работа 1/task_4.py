users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
OK = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
OK = {
    "Общее количество": len(users),
    "Уникальные посещения": len(set(users))
    }
print(OK)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
