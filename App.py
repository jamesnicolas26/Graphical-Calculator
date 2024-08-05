import tkinter as tk


class Calculator:
    """A simple graphical calculator application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        # Entry widget to display the expression
        self.entry = tk.Entry(self.root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        """Create calculator buttons."""
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in button_texts:
            button = tk.Button(self.root, text=text, width=10, height=3, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, char):
        """Handle button click events."""
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif char in '0123456789+-*/.':
            self.expression += char
        else:
            self.expression = ""

        self.update_entry()

    def update_entry(self):
        """Update the entry widget with the current expression."""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
