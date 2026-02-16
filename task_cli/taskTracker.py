from task_cli import jsonFile
from datetime import datetime

dataManipulation = jsonFile.DataManipulation()

class Task:
    def __init__(self, id: int, desc: str):
        """
        Setting the structure for Tasks
        
        :param self: Description
        :param id: Description
        :type id: int
        :param desc: Description
        :type desc: str
        """
        self.id = id
        self.desc = desc
        self.status = ['todo', 'in-progress', 'done']
        self.createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
        # Appending new Task to 
        data.append(record)

        dataManipulation.insert_into_JSON(data)

        print(f"Task added successfully (ID: {new_id})")

