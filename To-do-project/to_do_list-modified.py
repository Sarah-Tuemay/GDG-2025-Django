import json
class ToDO:
    def load_todos(self):
        with open("Python_Json/to_do.json", "r") as file:
            todos = json.load(file)
        return todos
    def addTask(self):
        todo_list = self.load_todos()
        length = len(todo_list) + 1
        
        title = input("Enter the task: ")
        task = {
            "title": title,
            "id":length,
            "completed": False
        }
        todo_list.append(task)
        # saving the new files
        with open("Python_Json/to_do.json", "w") as f:
            json.dump(todo_list, f, indent=2)
    def viewTasks(self):
        todo_list = self.load_todos()
        if len(todo_list) == 0:
            print("There are no tasks yet!")
        else:
            for todo in todo_list:
                print(f"Task: {todo['title']}")
                print(f"TaskId: {todo['id']}")
                print(f"Task-status: {todo['completed']}")
    def updateTask(self):
        todo_list = self.load_todos()
        id = int(input("Enter the id of the task you want to update: "))
        for todo in todo_list:
            if todo['id'] == id:
                print("What do you want to update? ")
                print("1. Title of the task")
                print("2. Mark status as completed")
                choice = int(input(""))
                if choice == 1:
                    new_title = input("Enter the new-title")
                    todo['title'] = new_title
                elif choice == 2:
                    todo['completed'] = True
                else: 
                    print("Invalid input")
                with open("Python_Json/to_do.json", "w") as file:
                    json.dump(todo_list, file, indent=2)
                return
       
            print(f"There is no task with id {id}")
        
    def deleteTask(self):
        todo_list = self.load_todos()
        id = int(input("Enter the id of the task you want to delete: "))
        for todo in todo_list:
            if todo['id'] == id:
                todo_list.remove(todo)
                return     
        print(f"There is no task with id {id}")

todo = ToDO()

while True:
    print("1. ADD Task: ")
    print("2. View Tasks: ")
    print("3. Update Task: ")
    print("4. Delete Task: ")
    print("5. Exit ")
    choice = input("Enter your choice: ")

    if choice == "1":
        todo.addTask()
    elif choice == "2":
        todo.viewTasks()
    elif choice == "3":
        todo.updateTask()
    elif choice == "4":
        todo.deleteTask()
    elif choice == "5":
        break
    else:
        print("Invalid choice")         