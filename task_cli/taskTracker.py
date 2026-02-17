from task_cli import jsonFile
from datetime import datetime

dataManipulation = jsonFile.DataManipulation()


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
        # Increment id by 1
        new_id = len(data) + 1
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
