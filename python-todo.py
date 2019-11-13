# keep track of todos using a list.
todo_list = []
#add todos
def add_todo(todo):
    todo_list.append(todo)

def del_todo(todo):
    del todo_list[todo]

def print_todo():
    if todo_list == []:
        print("you did it all. find more to do.")
    else:
        for x in range(len(todo_list)):
            print(f"{x}. {todo_list[x]}")

# i need to be able to delete todods.
def delete_todo(index):
    try:
        todo_list.pop(index)
    except IndexError:
        print("Sorry, no to do at that index")

def main():
    menu ="""
A simple little python to do list app
+++++++++++++++++++++++++++++++++++++
0. Quit
1. Print the To do list
2. Add a to do list
3. Complete a To Do
"""
    is_running = True
    while is_running:
        print(menu)
        selection = input("What would you like to do? ")
        if selection == '0':
            is_running = False
            print("BYEEEEEE!!!!!!")
        elif selection == '1':
            print_todo()
        elif selection == '2':
            add_todo(input("what do you need to do?"))

        elif selection == '3':
            print_todo()
            del_todo(int(input("gimme the number of the thing you did : ")))
        else:
            print("pick a real thing this time")
        

main()