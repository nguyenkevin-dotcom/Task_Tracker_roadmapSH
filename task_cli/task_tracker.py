# Copyright (c) 2026 nguyenkevin-dotcom
#
# -*- coding:utf-8 -*-
# @Script: json_file.py.py
# @Author: nguyenkevin-dotcom
# @Email: nguk0907@gmail.com
# @Create At: 2026-02-19 00:26:45
# @Last Modified By: nguyenkevin-dotcom
# @Last Modified At: 2026-02-19 16:55:50
# @Description: This file works with commands of Task Tracker project.
# Trying to handle edge cases and errors.
# For creating and formatting date and time I am using
# from standard python library datetime.

from task_cli import json_file
from datetime import datetime

# Getting the function from class DataManipulation
dataManipulation = json_file.DataManipulation()


class Task:
    def __init__(self):
        self.status = ["todo", "in-progress", "done"]

    def add(self, desc: str):
        """
        Adding new task into the JSON file.

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
                    "The description can't be named same as previously created Tasks."
                )
                return

        if len(desc) > 13:
            print(
                "The text of description is too long! The maximum number of characters is 13."
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
        # Return message
        print(f"Task added successfully (ID: {new_id}).")

    def update(self, id: int, updatedDesc: str):
        """
        Update the description of existing tasks.

        :param self: Description
        :param id: Description
        :type id: int
        :param updatedDesc: Description
        :type updatedDesc: str
        """
        data = dataManipulation.read_everything()
        for i in range(len(data)):
            if data[i]["id"] == id:
                if data[i]["description"] == updatedDesc:
                    print("The description is same as the current one.")
                    return
                else:
                    data[i]["description"] = updatedDesc
                    data[i]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    dataManipulation.insert_into_JSON(data)
                    print(f"The description of task (ID: {id}) has been changed.")
                    return
        print(f"The task (ID: {id}) does not exist.")

    def delete(self, id: int):
        """
        Delete tasks by their id.

        :param self: Description
        :param id: Description
        :type id: int
        """
        data = dataManipulation.read_everything()
        for index, task in enumerate(data):
            if task["id"] == id:
                del data[index]
                print(f"The task (ID: {id}) has been deleted.")
                dataManipulation.insert_into_JSON(data)
                return
        print(f"The task (ID: {id}) does not exist or has been already deleted.")

    def mark_in_progress(self, id: int):
        """
        Set label status to [ in-progress ].

        :param self: Description
        :param id: Description
        :type id: int
        """
        data = dataManipulation.read_everything()
        for task in data:
            if task["id"] == id:
                if task["status"] == self.status[1]:
                    print(f"The task has already been set to [ {self.status[1]} ]")
                    return
                elif task["status"] != self.status[1]:
                    task["status"] = self.status[1]
                    task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    dataManipulation.insert_into_JSON(data)
                    print(f"The task (ID: {id}) is set to [ {self.status[1]} ]")
                    return
        print(f"The task (ID: {id}) does not exist")

    def mark_done(self, id: int):
        """
        Set label status to [ done ].

        :param self: Description
        :param id: Description
        :type id: int
        """
        data = dataManipulation.read_everything()
        for task in data:
            if task["id"] == id:
                if task["status"] == self.status[2]:
                    print(f"The task has already been set to [ {self.status[2]} ]")
                    return
                elif task["status"] != self.status[2]:
                    task["status"] = self.status[2]
                    task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    dataManipulation.insert_into_JSON(data)
                    print(f"The task (ID: {id}) is set to [ {self.status[2]} ]")
                    return
        print(f"The task (ID: {id}) does not exist")

    def list(self, *items):
        """
        List tasks, it is also possible to list tasks based by their status.

        Possible commands:
        task-cli list => prints every existing task
        task-cli list todo => prints every existing task with status [ todo ]
        task-cli list in-progress => prints every existing task with status [ in-progress ]
        task-cli list done => prints every existing task with status [ done ]

        :param self: Description
        :param items: Not necessary, it can take more arguments
        """
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
            status_options = " | ".join(
                f"{self.status[i]}" for i in range(len(self.status))
            )
            print(
                f"!! The only arguments the list command takes are [ {status_options} ]"
            )
