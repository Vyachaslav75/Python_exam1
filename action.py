import view as v
import controller as c
import datetime as dt


def new_note():
    new_msg = ['Заголовок', 'Сообщение']
    new_msg = v.input_data(new_msg)
    if len(c.note['notes']) == 0:
        c.note['notes'].append({
            'id': 1,
            'title': new_msg[0],
            'mesg': new_msg[1],
            'date': dt.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
        })
    else:
        c.note['notes'].append({
            'id': c.note['notes'][len(c.note['notes']) - 1]['id'] + 1,
            'title': new_msg[0],
            'mesg': new_msg[1],
            'date': dt.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
        })


def delete_note():
    id = v.input_data([' id для удаления'])
    i = find_index(int(id[0]))
    if i > 0:
        c.note['notes'].pop(i)


def find_index(id):
    find = False
    i = 0
    # print(c.note)
    while (not find) and (i < len(c.note['notes'])):
        if c.note['notes'][i]['id'] == id:
            find = True
            return i
        i += 1
    return -1


def edit_note():
    id = v.input_data([' id для редактирования'])
    i = find_index(int(id[0]))
    if i > 0:
        v.show_data(c.note['notes'][i])
        new_msg = ['Заголовок', 'Сообщение']
        new_msg = v.input_data(new_msg)
        c.note['notes'][i]['title'] = new_msg[0]
        c.note['notes'][i]['mesg'] = new_msg[1]
        note_date = dt.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
        c.note['notes'][i]['date'] = note_date


def view_note():
    id = v.input_data([' id для просмотра'])
    i = find_index(int(id[0]))
    if i > 0:
        v.show_data(c.note['notes'][i])


def view_all_notes():
    for i in c.note['notes']:
        v.show_data(i)


def choose_date():
    dt_choose1 = v.input_data([' дату начальную в формате yyyy-mm-dd'])
    dt_choose2 = v.input_data([' дату конечную в формате yyyy-mm-dd'])
    for i in c.note['notes']:
        if dt_choose1[0] < i['date'] < dt_choose2[0]:
            v.show_data(i)
