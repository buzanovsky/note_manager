note = [
    "Имя пользователя",
    "Содежание заметки",
    "Статус",
    "Дата создания",
    "Дата изменения",
    ["Заголовок 1", "Заголовок 2", "Заголовок 3"]
]
titles =  note[5]


note[0] = input('Введите имя пользователя: ')
note[1] = input('Введите текст заметки: ')
note[2] = input('Введите в качестве статуса заметки "активна" или "не активна": ')
note[3] = input('Введите дату создания в формате дд.мм.гггг: ')
note[4] = input('Введите дату истечения заметки в формате дд.мм.гггг: ')
titles[0] = input('Заголовок 1: ')
titles[1] = input('Заголовок 2: ')
titles[2] = input('Заголовок 3: ')


print("Имя пользователя: ", note[0])
print("Содержание заметки: ", note[1])
print("Статус: ", note[2])
print("Дата создания: ", note[3])
print("Дата изменения: ", note[4])
print('Заголовок 1: ', titles[0])
print('Заголовок 2: ', titles[1])
print('Заголовок 3: ', titles[2])
