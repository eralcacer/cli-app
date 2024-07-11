import click


@click.group()
def mycommands():
    pass


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")


PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial",
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0) # Do not need to specify the path file
@click.option("-n", "--name", prompt="Enter the todo name", help="The name of the todo item")
@click.option("-d", "--desc", prompt="Describe the todo", help="Description of the todo item")
def add_todo(name, desc, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"

    with open(filename, "r") as f:
        is_first_entry = f.read().strip() == ""
    with open(filename, "a+") as f:
        if not is_first_entry:
            f.write("\n")
        f.write(f"{name}: {desc} [Priority: {PRIORITIES[priority]}]")


@click.command()
@click.argument("index", type=int, required=1)
@click.argument("todofile", type=click.Path(exists=True), required=0)
def delete_todo(index, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
        if len(todo_list)-1 < index:
            print(f"Index {index} out of range in the file. Only {len(todo_list)} items exist")
            return
        todo_list.pop(index)
    with open(filename, "w") as f:
        f.write("\n".join(todo_list))

@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()

    if priority is None:
        for index, todo in enumerate(todo_list):
            print(f"{index} - {todo}")
    else:
        for index, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"{index} - {todo}")


mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)

if __name__ == "__main__":
    mycommands()