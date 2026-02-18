import argparse
from task_cli.task_tracker import Task


def main():

    # Introduction of my CLI
    parser = argparse.ArgumentParser(
        description = "Task manager",
        epilog = "Command example: \033[1m"
        + 'task-cli add "Description of the task"'
        + '\033[0m => it will create a new task with description: "Description of the task"',
    )

    # Creating space for my commands
    subparsers = parser.add_subparsers(title="Operators", dest="operator")

    # Command add
    add = subparsers.add_parser("add", help = "Adding task")
    add.add_argument("desc", type = str, help = "A short description of the task")

    # Command update
    update = subparsers.add_parser(
        "update", help = "Updating existing task with choosing their id"
    )
    update.add_argument("id", type = int, help = "ID of the task")
    update.add_argument(
        "updatedDesc", type = str, help = "A short description of the updating task"
    )

    # Command delete
    delete = subparsers.add_parser("delete", help = "Delete existing task by id")
    delete.add_argument("id", type = int, help = "ID of the task")

    # Command mark-in-progress
    in_progress = subparsers.add_parser(
        "mark-in-progress", help = "Change status from [ todo ] to [ in-progress ]"
    )
    in_progress.add_argument("id", type = int, help = "ID of the task")

    # Command mark-done
    done = subparsers.add_parser(
        "mark-done", help = "Change status from [ todo ] to [ in-progress ]"
    )
    done.add_argument("id", type = int, help = "ID of the task")

    list = subparsers.add_parser("list", help = "list created tasks, can also choose by their status [ todo | in-progress | done ]")
    list.add_argument("type_status", type = str, help = "choose task based on status", nargs = '?', default = "")

    # The text I have written
    args = parser.parse_args()

    task = Task()
    # What is appearing after text "task-cli"
    if args.operator == "add":
        task.add(args.desc)
    elif args.operator == "update":
        task.update(args.id, args.updatedDesc)
    elif args.operator == "delete":
        task.delete(args.id)
    elif args.operator == "mark-in-progress":
        task.mark_in_progress(args.id)
    elif args.operator == "mark-done":
        task.mark_done(args.id)
    elif args.operator == "list":
        task.list(args.type_status)
    else:
        parser.print_help()


# This says execute these codes on this file only when the person starts this code on this file
if __name__ == "__main__":
    main()
