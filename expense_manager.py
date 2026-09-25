class ExpenseManager:

    def __init__(self, database):

        self.database = database

    def get_expenses(self):

        return self.database.get_all_expenses()

    def get_expense(self, expense_id):

        return self.database.get_expense(
            expense_id
        )

    def add_expense(
        self,
        amount,
        category,
        description,
        expense_date
    ):

        self.database.add_expense(
            amount,
            category,
            description,
            expense_date
        )

    def update_expense(
        self,
        expense_id,
        amount,
        category,
        description,
        expense_date
    ):

        self.database.update_expense(
            expense_id,
            amount,
            category,
            description,
            expense_date
        )

    def delete_expense(self, expense_id):

        self.database.delete_expense(
            expense_id
        )

    def search_expenses(self, search_term):

        return self.database.search_expenses(
            search_term
        )

    def get_total(self):

        return self.database.get_total()

    def get_category_totals(self):

        return self.database.get_category_totals()