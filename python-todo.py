# keep track of todos using a list.
todo_list = []
#add todos
def add_todo(todo):
    todo_list.append(todo)

# prints empty list
print(todo_list)
#add todo by calling func
add_todo("feed the cat")
#print again
print(todo_list)