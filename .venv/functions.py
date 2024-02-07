def get_todo_file(filepath='todos.txt'):    # read the todos text file
    with open(filepath, 'r') as file:
        todo_file_local = file.readlines()
        return todo_file_local

def write_todo_file(filepath='todos.txt', todo_arg=[]):    # write on todos text file
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
        return

if __name__ == '__main__':
    print('Hello')
    print(get_todo_file())