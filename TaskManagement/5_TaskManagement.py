class Task:
    def __init__(self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

class TaskManagement:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title, description):
        for task in self.tasks:
            if task.task_id == task_id:
                print("Error: Task ID already exists.")
                return
        new_task = Task(task_id, title, description, "Pending")
        self.tasks.append(new_task)

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return
        print("Error: Task ID not found.")

    def update_status(self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = new_status
                return
        print("Error: Task ID not found.")

    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task.__dict__

task_manager = TaskManagement()

# Test case 1: Add a task
task_manager.add_task(1, "Implement feature X", "Implement new feature X in the project")
task_manager.add_task(2, "Fix bug Y", "Fix the bug Y reported by QA team")
task_manager.add_task(3, "Write documentation", "Write documentation for the project")

# Test case 2: Get task information
print(task_manager.get_task(2))
# Expected output: {'title': 'Fix bug Y', 'description': 'Fix the bug Y reported by QA team', 'status': 'pending'}

# Test case 3: Update task status
task_manager.update_status(2, "completed")
print(task_manager.get_task(2))
# Expected output: {'title': 'Fix bug Y', 'description': 'Fix the bug Y reported by QA team', 'status': 'completed'}

# Test case 4: Remove a task
task_manager.remove_task(1)
print(task_manager.get_task(1))
# Expected output: None