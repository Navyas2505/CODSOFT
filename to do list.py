import os

class TodoApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("To-Do List Application")
        print("======================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        print("======================")

    def view_tasks(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your Tasks:")
        print("======================")
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. {task}")
        print("======================")
        input("Press Enter to return to the main menu...")

    def add_task(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        new_task = input("Enter the new task: ")
        self.tasks.append(new_task)
        print("Task added successfully!")
        input("Press Enter to return to the main menu...")

    def update_task(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.view_tasks()
        try:
            task_index = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_index < len(self.tasks):
                new_task = input("Enter the updated task: ")
                self.tasks[task_index] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid input! Please enter a number.")
        input("Press Enter to return to the main menu...")

    def delete_task(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.view_tasks()
        try:
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks.pop(task_index)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid input! Please enter a number.")
        input("Press Enter to return to the main menu...")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    app = TodoApp()
    app.run()

