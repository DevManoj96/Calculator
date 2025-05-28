import tkinter as tk
from tkinter import messagebox
import time


is_dark = False

def update_option_menu_colors(menu_widget, bg, fg):
    menu_widget.config(bg=bg, fg=fg, highlightthickness=0, relief="flat")
    menu_widget["menu"].config(bg=bg, fg=fg)
def toggle_theme():
    global is_dark, operations_menu

    bg_color = "#222222" if not is_dark else "lightgray"
    fg_color = "white" if not is_dark else "black"

    root.configure(bg=bg_color)
    text_widgets = [heading1, label1, label2, result_area, submit_btn, toggle_btn, clear_btn, exit_btn]

    for widget in text_widgets:
         widget.configure(bg=bg_color, fg=fg_color)

    entry_widgets = [num1_entry, num2_entry]
    for entry in entry_widgets:
        entry.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    
    update_option_menu_colors(operations_menu, bg_color, fg_color)
    is_dark = not is_dark

def calc_menu(event=None):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Enter valid numbers please !!")
        return
    
    sign = selected_operations.get()


    if sign == "+":
        result = num1 + num2
        

    elif sign == "-":
        result = num1 - num2
        

    elif sign == "*":
        result = num1 * num2
        

    elif sign == "/":
        if num2 == 0:
            messagebox.showwarning("Warning", "Can't divide with Zero !!")
            result_area.config(text="")
            return
        else:                    
            result = num1 / num2
    else:
        messagebox.showerror("Error", "Invalid Operation")
        return

    result_area.config(text=f"Result: {result} ")        

def clear_fields():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_area.config(text="")
root = tk.Tk()
root.title("--- Calculator ---")
root.geometry('800x600')
root.resizable(True, True)

operations = ["+", "-", "*", "/"]

heading1 = tk.Label(root, text="Welcome to Calculator", font=("Arial", 12, "bold"), width=20, height=2)
heading1.pack(pady=5)

label1 = tk.Label(root, text="Enter first number :", font=("Arial", 12), width=20, height=2)
label1.pack(pady=5)

num1_entry = tk.Entry(root, justify='center', font=("Arial", 12))
num1_entry.pack(pady=5)

selected_operations = tk.StringVar()
selected_operations.set(operations[0])

operations_menu = tk.OptionMenu(root, selected_operations, *operations)
operations_menu.pack(pady=5)


label2 = tk.Label(root, text="Enter second number :", font=("Arial", 12), width=20, height=2)
label2.pack(pady=5)

num2_entry = tk.Entry(root, justify='center', font=("Arial", 12))
num2_entry.pack(pady=5)


result_area = tk.Label(root, text="", font=("Arial", 12))
result_area.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", command=calc_menu, font=("Arial", 12), width=20, height=2)
submit_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear", command=clear_fields, font=("Arial", 12), width=20, height=2)
clear_btn.pack(pady=5)

toggle_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme, font=("Arial", 12), width=20, height=2)
toggle_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12) ,width=20, height=2)
exit_btn.pack(pady=5)

root.bind('<Return>', calc_menu)

if __name__ == '__main__':
    root.mainloop()
