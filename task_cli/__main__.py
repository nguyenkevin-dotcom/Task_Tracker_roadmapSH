import argparse
from task_cli.taskTracker import Task

def main():
    # Introduction of my CLI
    parser = argparse.ArgumentParser(description = "Task manager", epilog = "Command example: \033[1m" + "task-cli add \"Description of the task\"" + "\033[0m")
    
    # Creating space for my commands
    subparsers = parser.add_subparsers(title = "Operators", dest = "operator")

    # Command add
    add_parser = subparsers.add_parser("add", help = "Adding task")
    add_parser.add_argument("desc", type = str, help = "A short description of the task")

    # The text I have written
    args = parser.parse_args()

    # What is appearing after text "task-cli"
    if args.operator == "add":
        task = Task(id = 1, desc = args.desc)
        task.add(args.desc)
    else:
        parser.print_help()

# This says execute these codes on this file only when the person starts this code on this file
if __name__ == "__main__":
    main()
