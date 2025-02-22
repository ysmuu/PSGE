import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_digits=True, use_specials=True):
    if length <= 0:
        raise ValueError("Password length must be greater than zero.")
    
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    
    password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    return password

def generate_and_display():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_specials = specials_var.get()
        password = generate_password(length, use_digits, use_specials)
        result_label.config(text=f"Generated Password: {password}", fg="green")
        copy_button.config(state=tk.NORMAL)
        copy_button.password = password
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive integer for password length.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(copy_button.password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

digits_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include digits", variable=digits_var, font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
tk.Checkbutton(root, text="Include special characters", variable=specials_var, font=("Arial", 12), bg="#f0f0f0").pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_and_display)
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#008CBA", fg="white", state=tk.DISABLED, command=copy_to_clipboard)
copy_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
