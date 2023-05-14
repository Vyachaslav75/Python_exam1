import view as v
import action as a
import work_file as wf

note = {}
# note['notes'] = []
try:
    note = wf.import_file()
    
except:
    note['notes'] = []

def start():
    
    while True:
        flag = v.user_interface()
        if flag == '1':
            a.new_note()
        elif flag == '2':
            a.edit_note()
        elif flag == '3':
            a.delete_note()
        elif flag == '4':
            a.view_note()
        elif flag == '5':
            a.choose_date()
        elif flag == '6':
            a.view_all_notes()
        elif flag == '7':
            wf.export_file(note)
            break
