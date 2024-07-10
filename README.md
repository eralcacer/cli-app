# CLI Application

This is a CLI Application that works with Python. It simulates a command line application to add, delete, and view todos into a ".txt" file.

# How to use?

Priority list:
  -o => Optional
  -l => Low
  -m => Medium
  -h => High
  -c => Crucial

To insert new todos to a file you can insert: (By default all new tasks priority level is assigned to medium and written to a file "mytodos.txt")

  python main.py add-todo
    Inserts a new todo inputting a name for the todo and a description. By default, it sets the priority of the item to Medium(m)

  python main.py add-todo --name "Name of the todo item"
    Inserts a new todo inputting a name for the todo and asking for a description. By default, it sets the priority of the item to Medium(m)
  python main.py add-todo --name "Name todo item" --desc "Description of the todo task" level-of-priority
    Insert a new todo inputting a name for the todo and a description and you can select the level of priority based on the list below (o, l, m, h, c)
  python main add-todo --name "Name to-do item" --desc "Description for the task" level-of-priority filename.txt
    Insert a new todo inputting a name for the todo and a description and you can select the level of priority based on the list below (o, l, m, h, c).
    It also specifies the name of the file where to store the to-do item.

To view the items list: (By default it looks for the items in the "mytodos.txt" file)

  python main.py list-todos
    Displays the list of items in the "mytodos.txt" file with an index from 0 to the last item

  python main.py list-todos -p level-of-priority
    Displays the list of items with the specified priority in the "mytodos.txt" file with an index from 0 to the last item

  python main.py list-todos filename.txt
    Displays the list of items in the specified file with an index from 0 to the last item

  python main.py list-todos filename.txt -p level-of-priority
    Displays the list of items in the specified file with the specified priority level an index from 0 to the last item

Delete a task from the document:

  python main.py delete-todo index
    Deletes the todo task from the "mytodos.txt" file in the specified index

# What did I learn?

💡 I learned to create a command line app that simulates a terminal

💡 I learned about Click library

💡 I learned the difference between "click.Options()" and "click.Arguments()"

## Dependencies

-Click
