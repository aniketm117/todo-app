import functions as func
import PySimpleGUI as sg
from functions import get_todo_file, write_todo_file
from time import strftime as time_n


label = sg.Text('Type a to-do item')
input_box = sg.InputText(tooltip='To-do Item', key='todo')

add_button = sg.Button("Add")

win = sg.Window('To-do App',
                layout=[[label],[input_box, add_button]],
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

            """with open('todos.txt','r') as file:
                todo_file = file.readline()
            
            todo_file.append(todo_file_text)

            with open('todos.txt','w') as file:
                file.writelines(todo_file)
            
            todo_list.append(todo_text) #list append operation end"""

        case 'Show' | 'show':
            # for v in todo_list: #list is empty at start
            #    print(str(todo_list.index(v) + 1) + '. ' + v)

            # file = open('todos.txt', 'r')  # open the txt file in read mode
            # todo_file = file.readlines()  # list of items
            # for v in todo_file: #iterate
            #     print(str(todo_file.index(v) + 1) + '. ' + v.strip('\n'))
            # file.close()

            """with open('todos.txt','r') as file:
                todo_file = file.readlines()
                print(type(todo_file))

                for index, item in enumerate(todo_file):
                    item_n = item.strip('\n')
                    item_row = f"{index + 1}-{item_n}"
                    print(item_row)"""

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
                todo_file = func.get_todo_file('todos.txt')

                for index, item in enumerate(todo_file):
                    item_n = item.strip('\n')
                    item_row = f"{index + 1}-{item_n}"
                    print(item_row)

                k = int(key_val['todo'])  # to-do item to be edited

                todo_file = func.get_todo_file('todos.txt')

                for index, item in enumerate(todo_file):
                    if index == k - 1:
                        todo_edit_item_upd = input('Enter the item you want to replace ' + item.strip('\n') + ' with :')
                        todo_file[k - 1] = todo_edit_item_upd + '\n'

                func.write_todo_file('todos.txt', todo_file)

            except ValueError:
                print('Command not compatiable')
                continue

            except IndexError:
                print('Command not compatiable')
                continue
            """j = 0
            for item in todo_list:

                if item == todo_edit_item:
                    todo_edit_item_upd = input('Enter the item you want to replace ' + todo_list[k-1] + ' with :')
                    todo_list[k-1] = todo_edit_item_upd
                    break
                else:
                    j += 1 #item not found counter"""

        case 'Complete' | 'complete':

            todo_file = func.get_todo_file('todos.txt')

            for index, item in enumerate(todo_file):
                item_n = item.strip('\n')
                item_row = f"{index + 1}-{item_n}"
                print(item_row)

            k = int(key_val['todo'])  # row int to be completed

            todo_file = func.get_todo_file('todos.txt')

            print("Well done! You have completed the task {0}".format(todo_file.pop(k - 1)))

            func.write_todo_file('todos.txt', todo_file)

        case sg.WIN_CLOSED:
            break

    """g = input('Continue (Y/N) ?')
    if g == 'Y' or g == 'y':
        continue
    else:
        print('You entered ' + str(i) +' items to the list. Have a good day!')
        break"""

win.close()