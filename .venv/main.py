# use of if-elif-else statements instead of match
from functions import get_todo_file, write_todo_file
from time import strftime as time_n

prompt = 'What is your name ? '

nam = input(prompt)
print('Your name is ' + str(nam) +', Slim Shady')

# prompt1 = 'Enter a item in To-do list: ' redundant prompt

# todo_list = []

i = 0 #add count
while True:

    print("Hello "  + str(nam) + "! It is " + time_n("%b %d, %Y %H:%M:%S") + ". Type" + \
     "'show 0' if you want to see the full to-do list")

    user_action = input('Or, you may type add, edit, show or complete and' + \
                        ' the to-do item/number seperated by a space: ')
    user_action.strip()


    if user_action.startswith('add'):
        todo_file_text = user_action[4:] + "\n" #string to be appended text file

        print('You entered: ' + todo_file_text)
        i += 1

        todo_file = get_todo_file()

        todo_file.append(todo_file_text)

        write_todo_file('todos.txt',todo_file)

    elif user_action.startswith('edit'):

        try:
            todo_file = get_todo_file('todos.txt')
            # print(type(todo_file)) file type

            for index, item in enumerate(todo_file):
                item_n = item.strip('\n')
                item_row = f"{index + 1}-{item_n}"
                print(item_row)

            k = int(user_action[5]) #to-do item to be edited


            todo_file = get_todo_file('todos.txt')

            for index, item in enumerate(todo_file):
                if index == k-1:
                    todo_edit_item_upd = input('Enter the item you want to replace ' + item.strip('\n') + ' with :')
                    todo_file[k-1] = todo_edit_item_upd + '\n'

            write_todo_file('todos.txt', todo_file)

            """with open('todos.txt','w') as file:
                file.writelines(todo_file)"""

            """legacy
                j = 0
            for item in todo_list:
    
                if item == todo_edit_item:
                    todo_edit_item_upd = input('Enter the item you want to replace ' + todo_list[k-1] + ' with :')
                    todo_list[k-1] = todo_edit_item_upd
                    break
                else:
                    j += 1 #item not found counter"""

        except ValueError:
            print('Command not compatiable')
            continue

        except IndexError:
            print('Command not compatiable')
            continue

    elif user_action.startswith('show'):

        todo_file = get_todo_file('todos.txt')
        # print(type(todo_file)) file type

        for index, item in enumerate(todo_file):

            if int(user_action[5]) == 0:
                item_n = item.strip('\n')
                item_row = f"{index + 1}-{item_n}"
                print(item_row)
            elif int(user_action[5]) == index + 1:  #iterate once if not all items are to be shown
                item_n = item.strip('\n')
                item_row = f"{index + 1}-{item_n}"
                print(item_row)
                break #cease iteration

    elif user_action.startswith('complete'):

        todo_file = get_todo_file('todos.txt')

        for index, item in enumerate(todo_file):
            item_n = item.strip('\n')
            item_row = f"{index + 1}-{item_n}"
            print(item_row)

        k = int(user_action[9]) # row int to be completed

        todo_file = get_todo_file('todos.txt')

        print("Well done! You have completed the task {0}".format(todo_file.pop(k - 1)))

        write_todo_file('todos.txt',todo_file)

    else:
        print("Command not found")

    g = input('Continue (Y/N) ?') #exit ramp

    if g == 'Y' or g == 'y':
        continue
    else:
        print('You entered ' + str(i) +' items to the list. Have a good day!')
        break