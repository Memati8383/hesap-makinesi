import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi")

        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(self.root, textvariable=self.result_var, font=("Helvetica", 36), padx=20, pady=10)
        self.result_label.grid(row=0, column=0, columnspan=4)

        button_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in button_texts:
            button = tk.Button(self.root, text=text, font=("Helvetica", 16), padx=10, pady=10, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except:
                messagebox.showerror("Hata", "Geçersiz İfade")
        else:
            if current_text == "0":
                new_text = button_text
            else:
                new_text = current_text + button_text
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
