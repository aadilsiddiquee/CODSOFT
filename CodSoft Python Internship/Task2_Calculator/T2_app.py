import tkinter as tk
from tkinter import ttk

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "⌫":  # Backspace button
        entry.delete(len(current_text) - 1, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the input and result
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Configure row and column weights so that they expand proportionally
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('⌫', 5, 1)  
]

# Create and place the buttons with a modern style
style = ttk.Style()
style.configure('TButton', font=('Arial', 14))

for (text, row, column) in buttons:
    button = ttk.Button(root, text=text, style='TButton', command=lambda t=text: on_click(t))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

# Run the application
root.mainloop()
