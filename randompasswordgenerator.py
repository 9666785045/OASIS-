import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        #  input fields
        tk.Label(root, text="Password Length:").pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        tk.Label(root, text="Include Letters:").pack()
        self.letters_var = tk.IntVar()
        tk.Checkbutton(root, variable=self.letters_var).pack()

        tk.Label(root, text="Include Numbers:").pack()
        self.numbers_var = tk.IntVar()
        tk.Checkbutton(root, variable=self.numbers_var).pack()

        tk.Label(root, text="Include Symbols:").pack()
        self.symbols_var = tk.IntVar()
        tk.Checkbutton(root, variable=self.symbols_var).pack()

        #  generate button
        generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        generate_button.pack()

        #  label to display results
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Input Error", "Password length must be a positive integer.")
                return

            use_letters = self.letters_var.get() == 1
            use_numbers = self.numbers_var.get() == 1
            use_symbols = self.symbols_var.get() == 1

            password = self.generate_password_string(length, use_letters, use_numbers, use_symbols)
            self.result_label.config(text=f"Generated password: {password}")

        except ValueError:
            messagebox.showerror("Input Error", "Invalid input. Please enter a valid password length.")

    def generate_password_string(self, length, use_letters, use_numbers, use_symbols):
        char_set = ""
        if use_letters:
            char_set += string.ascii_letters
        if use_numbers:
            char_set += string.digits
        if use_symbols:
            char_set += string.punctuation

        password = ''.join(random.choice(char_set) for _ in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()