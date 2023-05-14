def user_interface():
    invite_str = '''Введите:
    1 для добавления новой заметки
    2 для редактирования заметки
    3 для удаления заметки
    4 для просмотра заметки
    5 для выборки по дате
    6 просмотра списка заметок
    7 для выхода\n'''
    print(invite_str)
    flag = input('Выберите действие:  ')
    return flag


def input_data(user_str):
    res = []
    for i in user_str:
        res.append(input(f'Введите {i}: '))
    return res


def show_data(data):
    print(data)
