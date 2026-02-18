from task_cli import json_file
from datetime import datetime

dataManipulation = json_file.DataManipulation()


class Task:
    def __init__(self):
        self.status = ["todo", "in-progress", "done"]

    def add(self, desc: str):
        """
        Adding new task into the JSON file

        :param self: Description
        :param desc: Description
        :type desc: str
        """
        # Firstly it will read the JSON file if there is something
        data = dataManipulation.read_everything()

        # Assure that when creating task it will not have an existing id
        new_id = 1

        ids = []

        for task in data:
            ids.append(task["id"])
        ids.sort()
        for i in range(len(ids)):
            if new_id == ids[i]:
                new_id += 1

        # Assure that description is not same as the existing ones
        for task in data:
            if task["description"] == desc:
                print(
                    "The description can't be named the samed as previously created Tasks"
                )
                return

        # Record of the new task
        record = {
            "id": new_id,
            "description": desc,
            "status": self.status[0],
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        # Appending new Task to
        data.append(record)
        dataManipulation.insert_into_JSON(data)

        print(f"Task added successfully (ID: {new_id})")

    def update(self, id: int, updatedDesc: str):
        data = dataManipulation.read_everything()
        for i in range(len(data)):
            if data[i]["id"] == id:
                data[i]["description"] = updatedDesc
                data[i]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dataManipulation.insert_into_JSON(data)

    def delete(self, id: int):
        data = dataManipulation.read_everything()
        for index, task in enumerate(data):
            if task["id"] == id:
                del data[index]
        dataManipulation.insert_into_JSON(data)

    def mark_in_progress(self, id: int):
        data = dataManipulation.read_everything()
        for task in data:
            if task["id"] == id:
                task["status"] = self.status[1]
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dataManipulation.insert_into_JSON(data)

    def mark_done(self, id: int):
        data = dataManipulation.read_everything()
        for task in data:
            if task["id"] == id:
                task["status"] = self.status[2]
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dataManipulation.insert_into_JSON(data)

    def list(self, *items):

        data = dataManipulation.read_everything()

        # Adjusting widths
        widths = [5, 15, 12, 22, 19]

        # Creating a new list for including only values based on status of tasks
        values = []

        # If command is task-cli list
        if items[0] == "":
            # Separating line between values and lines
            print("-" * sum(widths))

            # Creating a new list for including only labels
            labels = [label for label in data[0].keys()]
            header_row = "".join(
                f"{labels[i]:<{widths[i]}}" for i in range(len(labels))
            )
            print(header_row)

            # Separating line between values and lines
            print("-" * sum(widths))

            # Getting the values of task
            for task in data:
                value = [value for value in task.values()]
                values.append(value)

            # Formatting the obtained values of task
            for value in values:
                formatted_row = "".join(
                    f"{str(value[i]):<{widths[i]}}" for i in range(len(value))
                )
                print(formatted_row)

        # If command is task-cli list todo
        elif items[0] == "todo":
            # Separating line between values and lines
            print("-" * sum(widths))

            # Creating a new list for including only labels
            labels = [label for label in data[0].keys()]
            header_row = "".join(
                f"{labels[i]:<{widths[i]}}" for i in range(len(labels))
            )
            print(header_row)

            # Separating line between values and lines
            print("-" * sum(widths))

            # Getting the values of task that has status todo
            for task in data:
                if task["status"] == "todo":
                    value = [value for value in task.values()]
                    values.append(value)

            # Formatting the obtained values of task
            for value in values:
                formatted_row = "".join(
                    f"{str(value[i]):<{widths[i]}}" for i in range(len(value))
                )
                print(formatted_row)

        # If command is task-cli list in-progress
        elif items[0] == "in-progress":
            # Separating line between values and lines
            print("-" * sum(widths))

            # Creating a new list for including only labels
            labels = [label for label in data[0].keys()]
            header_row = "".join(
                f"{labels[i]:<{widths[i]}}" for i in range(len(labels))
            )
            print(header_row)

            # Separating line between values and lines
            print("-" * sum(widths))

            # Getting the values of task that has status in-progress
            for task in data:
                if task["status"] == "in-progress":
                    value = [value for value in task.values()]
                    values.append(value)

            # Formatting the obtained values of task
            for value in values:
                formatted_row = "".join(
                    f"{str(value[i]):<{widths[i]}}" for i in range(len(value))
                )
                print(formatted_row)

        # If command is task-cli list in-progress
        elif items[0] == "done":
            # Separating line between values and lines
            print("-" * sum(widths))

            # Creating a new list for including only labels
            labels = [label for label in data[0].keys()]
            header_row = "".join(
                f"{labels[i]:<{widths[i]}}" for i in range(len(labels))
            )
            print(header_row)

            # Separating line between values and lines
            print("-" * sum(widths))

            # Getting the values of task that has status done
            for task in data:
                if task["status"] == "done":
                    value = [value for value in task.values()]
                    values.append(value)

            # Formatting the obtained values of task
            for value in values:
                formatted_row = "".join(
                    f"{str(value[i]):<{widths[i]}}" for i in range(len(value))
                )
                print(formatted_row)
        else:
            print(
                "!! The only arguments the list command takes are [ todo | in-progress | done ] !!"
            )
