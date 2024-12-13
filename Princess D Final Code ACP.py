import tkinter as tk
from tkinter import messagebox


class FinancialTracker:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.savings_goal = 0
        self.savings = 0
        self.user_name = ""
        self.valid_id = ""

    def set_income(self, amount):
        self.income = amount

    def set_expenses(self, amount):
        self.expenses = amount

    def set_savings_goal(self, goal):
        self.savings_goal = goal

    def calculate_savings(self):
        self.savings = self.income - self.expenses
        return self.savings

    def check_financial_health(self):
        if self.savings >= self.savings_goal:
            return "Great job! Your savings goal is now a reality!"
        elif self.savings > 0:
            return "You're doing great, stay focused on your savings!"
        elif self.savings == 0:
            return "You're not losing money, but trimming some expenses could boost your savings."
        else:
            return "You're in a negative balance. Start slashing unnecessary expenses."

    def suggest_savings(self):
        if self.savings < 0:
            return "Review your spending and cut back on unnecessary costs to prevent future money problems."
        elif self.savings == 0:
            return "Start saving even a small amount to build your savings."
        else:
            return "Well done! Keep your savings going to create financial peace of mind."


class FinancialTrackerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FinTrack: A Personal Finance Management")
        self.geometry("700x500")

        self.default_font = ("Open Sans", 10)

        self.tracker = FinancialTracker()
        
        self.config(bg="lightblue")

        for i in range(4):
            self.columnconfigure(i, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.label_user_name = tk.Label(self, text="Name:", font=self.default_font, bg="lightblue")
        self.label_user_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_user_name = tk.Entry(self, font=self.default_font, bg="white")
        self.entry_user_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_valid_id = tk.Label(self, text="Valid ID:", font=self.default_font, bg="lightblue")
        self.label_valid_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.valid_id_options = ["SELECT", "Employee ID", "Student ID", "Voter's ID", "PhilHealth ID"]
        self.selected_valid_id = tk.StringVar(self)
        self.selected_valid_id.set(self.valid_id_options[0])
        self.dropdown_valid_id = tk.OptionMenu(self, self.selected_valid_id, *self.valid_id_options)
        self.dropdown_valid_id.config(font=self.default_font, bg="white")
        self.dropdown_valid_id.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.label_id_number = tk.Label(self, text="ID Number:", font=self.default_font, bg="lightblue")
        self.label_id_number.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_goal = tk.Entry(self, font=self.default_font, bg="white")
        self.entry_goal.grid(row=2, column=1, padx=0, pady=0, sticky="w")

        self.label_income = tk.Label(self, text="Monthly Income/Allowance:", font=self.default_font, bg="lightblue")
        self.label_income.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.entry_income = tk.Entry(self, font=self.default_font, bg="white")
        self.entry_income.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.label_expenses = tk.Label(self, text="Monthly Expenses:", font=self.default_font, bg="lightblue")
        self.label_expenses.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.entry_expenses = tk.Entry(self, font=self.default_font, bg="white")
        self.entry_expenses.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.label_goal = tk.Label(self, text="Savings Target:", font=self.default_font, bg="lightblue")
        self.label_goal.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        self.entry_goal = tk.Entry(self, font=self.default_font, bg="white")
        self.entry_goal.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        self.button_calculate = tk.Button(
            self, text="Calculate", font=self.default_font, bg="lightcoral", relief="groove", command=self.calculate_financials
        )
        self.button_calculate.grid(row=3, column=0, columnspan=4, pady=20)

        self.label_savings = tk.Label(self, text="Savings: Php 0.00", font=self.default_font, bg="lightcoral")
        self.label_savings.grid(row=4, column=0, columnspan=4, pady=10)

        self.label_health = tk.Label(self, text="Financial Strength: ", font=self.default_font, bg="lightcoral")
        self.label_health.grid(row=5, column=0, columnspan=4, pady=10)

        self.label_suggestion = tk.Label(self, text="Financial Tips: ", font=self.default_font, bg="lightcoral")
        self.label_suggestion.grid(row=6, column=0, columnspan=4, pady=10)

    def calculate_financials(self):
        try:
            name = self.entry_user_name.get().strip()
            valid_id = self.selected_valid_id.get()
            income = self.validate_numeric_input(self.entry_income.get(), "Monthly Income")
            expenses = self.validate_numeric_input(self.entry_expenses.get(), "Monthly Expenses")
            goal = self.validate_numeric_input(self.entry_goal.get(), "Savings Target")

            if not name or valid_id == "SELECT":
                raise ValueError("Please fill in your name and select a valid ID.")

            self.tracker.user_name = name
            self.tracker.valid_id = valid_id
            self.tracker.set_income(income)
            self.tracker.set_expenses(expenses)
            self.tracker.set_savings_goal(goal)

            savings = self.tracker.calculate_savings()
            self.label_savings.config(text=f"Savings: Php {savings:.2f}")

            financial_health = self.tracker.check_financial_health()
            self.label_health.config(text=f"Financial Strength: {financial_health}")

            suggestion = self.tracker.suggest_savings()
            self.label_suggestion.config(text=f"Financial Tips: {suggestion}")

        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Error: {e}")

    def validate_numeric_input(self, value, field_name):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"{field_name} must be a valid number.")


if __name__ == "__main__":
    app = FinancialTrackerGUI()
    app.mainloop()
