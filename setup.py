from setuptools import setup

setup(
    name="task-tracker",
    version="0.0.1",
    packages=["task_cli"],
    entry_points={
        "console_scripts": ["task-cli = task_cli.__main__:main"],
    },
    description="CLI app for managing your tasks",
    author="Kevin Nguyen",
    url="Hasn't done that yet",
    python_requires=">=3.6",
)
