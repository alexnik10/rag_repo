from task-manager import TaskManager

def main():
  taskManager = TaskManager()
  print("Welcome to TODO Manager!")
  while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
      taskTitle = input("Enter task title: ")
      taskDescription = input("Enter task description: ")
      taskManager.add-task(taskTitle, taskDescription)
    elif choice == "2":
      taskManager.view-tasks()
    elif choice == "3":
      taskId = input("Enter task ID to remove: ")
      taskManager.remove-task(taskId)
    elif choice == "4":
      fileName = input("Enter file name to save tasks: ")
      taskManager.save-tasks(fileName)
    elif choice == "5":
      fileName = input("Enter file name to load tasks: ")
      taskManager.load-tasks(fileName)
    elif choice == "6":
      print("Exiting TODO Manager. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
