from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from database import Database
from expense_manager import ExpenseManager


app = Flask(__name__)

database = Database()

expense_manager = ExpenseManager(database)




@app.route("/")
def index():

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        expenses = expense_manager.search_expenses(
            search
        )

    else:

        expenses = expense_manager.get_expenses()

    total = expense_manager.get_total()

    category_totals = (
        expense_manager.get_category_totals()
    )

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        category_totals=category_totals,
        search=search
    )




@app.route(
    "/add",
    methods=["GET", "POST"]
)
def add_expense():

    if request.method == "POST":

        amount = request.form["amount"]
        category = request.form["category"]
        description = request.form["description"]
        expense_date = request.form["date"]

        expense_manager.add_expense(
            amount,
            category,
            description,
            expense_date
        )

        return redirect(
            url_for("index")
        )

    return render_template(
        "add_expense.html"
    )




@app.route(
    "/edit/<int:expense_id>",
    methods=["GET", "POST"]
)
def edit_expense(expense_id):

    expense = expense_manager.get_expense(
        expense_id
    )

    if expense is None:

        return "Expense not found", 404

    if request.method == "POST":

        amount = request.form["amount"]
        category = request.form["category"]
        description = request.form["description"]
        expense_date = request.form["date"]

        expense_manager.update_expense(
            expense_id,
            amount,
            category,
            description,
            expense_date
        )

        return redirect(
            url_for("index")
        )

    return render_template(
        "edit_expense.html",
        expense=expense
    )




@app.route(
    "/delete/<int:expense_id>",
    methods=["POST"]
)
def delete_expense(expense_id):

    expense_manager.delete_expense(
        expense_id
    )

    return redirect(
        url_for("index")
    )




if __name__ == "__main__":

    app.run(debug=True)