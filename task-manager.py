from utils import generate-unique-id, format-task
from storage import Storage

class TaskManager:
  def __init__(self):
    self.taskList = []
    self.storage = Storage()

  def add-task(self, taskTitle, taskDescription):
    task = {
      "id": generate-unique-id(),
      "title": taskTitle,
      "description": taskDescription
    }
    self.taskList.append(task)
    print("Task added successfully!")

  def view-tasks(self):
    if not self.taskList:
      print("No tasks available.")
      return
    print("\nTasks:")
    for task in self.taskList:
      print(format-task(task))

  def remove-task(self, taskId):
    for task in self.taskList:
      if task["id"] == taskId:
        self.taskList.remove(task)
        print("Task removed successfully!")
        return
    print("Task not found.")

  def save-tasks(self, fileName):
    self.storage.save-to-file(fileName, self.taskList)
    print("Tasks saved successfully!")

  def load-tasks(self, fileName):
    loadedTasks = self.storage.load-from-file(fileName)
    if loadedTasks is not None:
      self.taskList = loadedTasks
      print("Tasks loaded successfully!")
    else:
      print("Failed to load tasks.")
