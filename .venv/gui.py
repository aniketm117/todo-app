import functions as func
import PySimpleGUI as sg
from functions import get_todo_file, write_todo_file
from time import strftime as time_n


label = sg.Text('Type a to-do item')
input_box = sg.InputText(tooltip='To-do Item', key='todo')

add_button = sg.Button("Add")

list_box = sg.Listbox(values=func.get_todo_file(),key='todo list',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

comp_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

win = sg.Window('To-do App',
                layout=[[label],[input_box, add_button],
                        [list_box, edit_button, comp_button],
                        [exit_button]],
                font={'Helvetica', 20}) #window instance
i = 0

while True:
    user_action, key_val = win.read() #read method to display the run
    print(user_action, key_val) #user_action is a string inst, key_val is a tuple inst

    match user_action:
        case 'Add' | 'add':
            #todo_text = input(prompt1) #string to be appended to list
            #todo_file_text = todo_text + "\n" #string to be appended text file
            todo_file_text = key_val['todo'] + "\n"

            todo_file = func.get_todo_file()

            todo_file.append(todo_file_text)

            func.write_todo_file('todos.txt', todo_file)

            print('You entered: ' + todo_file_text)
            i += 1

            win['todo list'].update(values=todo_file)  # updating the to-do list in listbox instance
            
            """with open('todos.txt','r') as file:
                todo_file = file.readline()
            
            todo_file.append(todo_file_text)

            with open('todos.txt','w') as file:
                file.writelines(todo_file)
            
            todo_list.append(todo_text) #list append operation end"""

        case 'Show' | 'show':

            todo_file = func.get_todo_file('todos.txt')

            for index, item in enumerate(todo_file):

                if int(key_val['todo']) == 0:
                    item_n = item.strip('\n')
                    item_row = f"{index + 1}-{item_n}"
                    print(item_row)
                elif int(key_val['todo']) == index + 1:  # iterate once if not all items are to be shown
                    item_n = item.strip('\n')
                    item_row = f"{index + 1}-{item_n}"
                    print(item_row)
                    break  # cease iteration

        case 'Edit' | 'edit':

            try:

                todo_edit_item = key_val['todo list'][0]
                todo_edit_item_upd = key_val['todo']

                todo_file = func.get_todo_file('todos.txt')

                for index, item in enumerate(todo_file):
                    if item == todo_edit_item:
                        #todo_edit_item_upd = input('Enter the item you want to replace ' + item.strip('\n') + ' with :')
                        todo_file[index] = todo_edit_item_upd + '\n'

                func.write_todo_file('todos.txt', todo_file)

                win['todo list'].update(values=todo_file) #updating the to-do list in listbox instance

            except ValueError:
                print('Command not compatiable')
                continue

            except IndexError:
                print('Command not compatiable')
                continue

        case 'Complete' | 'complete':

            todo_file = func.get_todo_file('todos.txt')

            item_comp = key_val['todo list'][0]  # row int to be completed

            todo_file.remove(item_comp)

            func.write_todo_file('todos.txt', todo_file)

            win['todo list'].update(values=todo_file)

        case 'todo list':
            win['todo'].update(value=key_val['todo list'][0])

        case sg.WIN_CLOSED | 'Exit':
            break

    """g = input('Continue (Y/N) ?')
    if g == 'Y' or g == 'y':
        continue
    else:
        print('You entered ' + str(i) +' items to the list. Have a good day!')
        break"""

win.close()