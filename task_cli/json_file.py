# Copyright (c) 2026 nguyenkevin-dotcom
#
# -*- coding:utf-8 -*-
# @Script: json_file.py
# @Author: nguyenkevin-dotcom
# @Email: nguk0907@gmail.com
# @Create At: 2026-02-19 00:24:15
# @Last Modified By: nguyenkevin-dotcom
# @Last Modified At: 2026-02-19 00:33:50
# @Description: This file focus on operations with JSON file. It consists of
# reading a JSON and inserting new values to existing JSON file.
# If JSON file does exit the program will create one.

import json
import os


class DataManipulation:
    def __init__(self, file="tasks.json"):
        self.file = file

    def read_everything(self):
        """
        Read a JSON file

        :param self: Description
        """
        # Check if there is file with a name that we set on variable file
        if not os.path.exists(self.file):
            return []
        # Reading JSON file
        with open(self.file, "r", encoding="UTF-8") as f:
            try:
                # file only with characters (no special characters)
                content = f.read().strip()
                if not content:
                    return []
                # return the items in JSON file
                return json.loads(content)
            except json.JSONDecodeError:
                return []

    def insert_into_JSON(self, data):
        """
        Insert new records into file (if the name of the file does
        not exist it will create one)

        :param self: Description
        :param data: Description
        """
        with open(self.file, "w", encoding="UTF-8") as task:
            json.dump(data, task, indent=4, ensure_ascii=False)
