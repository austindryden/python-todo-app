# keep track of todos using a list.
todo_list = []
#add todos
def add_todo(todo):
    todo_list.append(todo)

def del_todo(todo):
    del todo_list[index]

# prints empty list
print(todo_list)
#add todo by calling func
add_todo("feed the cat")
#print again
print(todo_list)

# i need to be able to delete todods.
def delete_todo(index):
    try:
        todo_list.pop(index)
    except IndexError:
        print("Sorry, no to do at that index")

def print_todo():
    for x in range(len(todo_list)):
        print(f"{x}. {todo_list[x]}")
