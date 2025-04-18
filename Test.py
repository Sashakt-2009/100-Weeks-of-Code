import tkinter as tk
import json as js
import os


class Tasks:
    def __init__(self, task_name, task_status="Pending"):
        self.task_name = task_name
        self.task_status = task_status

    def to_dict(self):
        return {"task_name": self.task_name, "task_status": self.task_status}


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
            self.tasks[index].task_status = "Completed"
            self.save_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                data = js.load(f)
                return [Tasks(**task) for task in data]
        except Exception:
            return []

    def save_tasks(self):
        with open(self.file_path, "w") as f:
            js.dump([task.to_dict() for task in self.tasks], f, indent=4)


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.manager = TaskManager("tasks.json")

        self.task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
        self.task_entry = tk.Entry(root, width=50)

        self.setup_ui()
        self.refresh_tasks()

    def setup_ui(self):
        self.root.title("TO-DO Manager")
        self.root.geometry("600x400")

        self.task_listbox.grid(padx=5, pady=20, rowspan=20)
        self.task_entry.grid(pady=10)

        tk.Button(self.root, text="Add Task", command=lambda: self.add_task).grid(column=1, row=1, padx=10)
        tk.Button(self.root, text="Remove Task", command=lambda: self.remove_task).grid(column=1, row=2, padx=10)
        tk.Button(self.root, text="Task Completed", command=lambda: self.complete_task).grid(column=1, row=3, padx=10)

    def add_task(self):
        name = self.task_entry.get().strip()
        if name:
            self.manager.add_task(name)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.manager.remove_task(selected[0])
            self.refresh_tasks()

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.manager.mark_completed(selected[0])
            self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            status = "✅" if task.task_status == "Completed" else "⏳"
            self.task_listbox.insert(tk.END, f"{status} {task.task_name}")


if __name__ == "__main__":
    app = TodoApp(tk.Tk())
    app.root.mainloop()
