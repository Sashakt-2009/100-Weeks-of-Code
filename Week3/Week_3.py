import tkinter as tk
from tkinter import ttk
import json as js
import os, sys

class Tasks:

    def __init__(self, task, status="pending"):
        self.task = task 
        self.status = status

    def to_dict(self):
        return {
            "task": self.task,
            "status": self.status
        }
    

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def add_task(self, task_name):
        task = Tasks(task_name)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = "completed"
            self.save_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                data = js.load(f)
                return [Tasks(**task) for task in data]
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []


    def save_tasks(self):
        with open(self.file_path, "w") as f:
            js.dump([task.to_dict() for task in self.tasks], f, indent=4)
        
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.manager = TaskManager(os.path.join(os.path.dirname(sys.argv[0]), "data/tasks.json")
)
        self.setup_ui()
        self.refresh_tasks()
        

    def setup_ui(self):
        
        self.root.title("Todo App")
        self.root.geometry("500x500")

        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=20)

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.mark_completed_button = tk.Button(self.root, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack(pady=5)

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.manager.add_task(task_name)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.manager.remove_task(index)
            self.refresh_tasks()

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.manager.mark_completed(index)
            self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            self.task_listbox.insert(tk.END, f" • {task.task}.....................({task.status})")

        

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
        