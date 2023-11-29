import functions


print("Welcome to the CLI Todo app!")

while True:

    # Print the current todo_list every iteration
    print("\nYour current todo list:")
    todos = functions.get_todos()
    functions.print_tasks()

    try:
        choice = input("\nWould you like to Add, Edit, Complete, or Exit?\n").lower().strip()

        # Add
        if choice.startswith("add"):
            todo = choice[len(choice.split(" ")[0])+1:]
            todos.append(todo)

        # Edit
        elif choice.startswith("edit"):
            todo = choice[len(choice.split(" ")[0])+1:]
            if todo in todos:
                change = input("\nWhat do you want to change this item to?\n")
                todos[todos.index(todo)] = change
            else:
                print("We couldn't find that todo.")

        # Complete
        elif choice.startswith("complete"):
            todo = choice[len(choice.split(" ")[0])+1:]
            if todo in todos:
                todos.remove(todo)
            else:
                print("We couldn't find that todo.")

        # Exit
        elif choice.startswith("exit") or choice.startswith("quit"):
            quit("\nSee you next time!")

        # Default
        else:
            print("Make sure to begin your command with a valid keyword")

        # Update file before obtaining new command
        functions.write_to_file(todos)

    except ValueError:
        print("Make sure to type a number if asked for one.")
