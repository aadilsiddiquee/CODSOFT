import os
import tkinter as tk
from tkinter import messagebox

def add_task(entry, tasks_listbox):
    new_task = entry.get()
    if new_task:
        tasks_listbox.insert(tk.END, new_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task(tasks_listbox):
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks(tasks_listbox):
    tasks_listbox.delete(0, tk.END)
    messagebox.showinfo("To-Do List", "All tasks cleared.")

def save_tasks_and_exit(app, tasks_listbox, filename="tasks.txt"):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, filename)

    tasks = tasks_listbox.get(0, tk.END)
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    messagebox.showinfo("To-Do List", f"Tasks saved to {filename}.")
    app.destroy()

def load_tasks(tasks_listbox, filename="tasks.txt"):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, filename)

    tasks_listbox.delete(0, tk.END)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            for task in tasks:
                tasks_listbox.insert(tk.END, task)

def main():
    app = tk.Tk()
    app.title("To-Do List App")

    entry = tk.Entry(app, width=40)
    entry.grid(row=0, column=0, padx=10, pady=10)

    add_button = tk.Button(app, text="Add Task", command=lambda: add_task(entry, tasks_listbox))
    add_button.grid(row=0, column=1, padx=10, pady=10)

    delete_button = tk.Button(app, text="Delete Task", command=lambda: delete_task(tasks_listbox))
    delete_button.grid(row=1, column=0, padx=10, pady=10)

    clear_button = tk.Button(app, text="Clear All", command=lambda: clear_tasks(tasks_listbox))
    clear_button.grid(row=1, column=1, padx=10, pady=10)

    save_button = tk.Button(app, text="Save and Exit", command=lambda: save_tasks_and_exit(app, tasks_listbox))
    save_button.grid(row=2, column=0, columnspan=2, pady=10)

    tasks_listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=50, height=10)
    tasks_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    load_tasks(tasks_listbox)

    app.mainloop()

if __name__ == "__main__":
    main()
