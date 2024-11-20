import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)
        category = categorize_bmi(bmi)

        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Setting up the main application window
app = tk.Tk()
app.title("BMI Calculator")

# Creating input fields
tk.Label(app, text="Weight (kg):").pack()
weight_entry = tk.Entry(app)
weight_entry.pack()

tk.Label(app, text="Height (m):").pack()
height_entry = tk.Entry(app)
height_entry.pack()

# Creating calculate button
calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# display results
result_label = tk.Label(app, text="")
result_label.pack()
app.mainloop()