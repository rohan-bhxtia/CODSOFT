import tkinter as tk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to perform the calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry field for the display
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create calculator buttons
button_1 = tk.Button(window, text="1", command=lambda: button_click(1), padx=20, pady=10)
button_2 = tk.Button(window, text="2", command=lambda: button_click(2), padx=20, pady=10)
button_3 = tk.Button(window, text="3", command=lambda: button_click(3), padx=20, pady=10)
button_4 = tk.Button(window, text="4", command=lambda: button_click(4), padx=20, pady=10)
button_5 = tk.Button(window, text="5", command=lambda: button_click(5), padx=20, pady=10)
button_6 = tk.Button(window, text="6", command=lambda: button_click(6), padx=20, pady=10)
button_7 = tk.Button(window, text="7", command=lambda: button_click(7), padx=20, pady=10)
button_8 = tk.Button(window, text="8", command=lambda: button_click(8), padx=20, pady=10)
button_9 = tk.Button(window, text="9", command=lambda: button_click(9), padx=20, pady=10)
button_0 = tk.Button(window, text="0", command=lambda: button_click(0), padx=20, pady=10)

button_add = tk.Button(window, text="+", command=lambda: button_click("+"), padx=20, pady=10)
button_subtract = tk.Button(window, text="-", command=lambda: button_click("-"), padx=20, pady=10)
button_multiply = tk.Button(window, text="", command=lambda: button_click(""), padx=20, pady=10)
button_divide = tk.Button(window, text="/", command=lambda: button_click("/"), padx=20, pady=10)

button_clear = tk.Button(window, text="C", command=clear, padx=20, pady=10)
button_equals = tk.Button(window, text="=", command=calculate, padx=20, pady=10)

# Place the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

# Run the Tkinter main loop
window.mainloop()
