import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x420")

# Display
screen = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
screen.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        # replace unicode operators with python operators
        expr = screen.get().replace("×", "*").replace("÷", "/")
        try:
            # safer eval: no builtins
            result = eval(expr, {"__builtins__": None}, {})
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        # if previous content was "Error", clear it before inserting
        if screen.get() == "Error":
            screen.delete(0, tk.END)
        screen.insert(tk.END, text)

# Buttons layout
buttons = [
    ["7","8","9","÷"],
    ["4","5","6","×"],
    ["1","2","3","-"],
    ["0",".","C","+"],
]

for r, row in enumerate(buttons, start=1):
    for c, btext in enumerate(row):
        btn = tk.Button(root, text=btext, font=("Arial", 18), width=4, height=2)
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", click)

# Equals button spanning the full width
eq = tk.Button(root, text="=", font=("Arial", 18), height=2)
eq.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
eq.bind("<Button-1>", click)

# Make grid cells expand nicely
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

root.mainloop()