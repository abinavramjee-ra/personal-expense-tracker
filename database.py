import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()



class Database:

    def __init__(self):

        self.config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE")
        }

    def connect(self):

        return mysql.connector.connect(
            **self.config
        )

    def get_all_expenses(self):

        connection = self.connect()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, amount, category, description, date
            FROM expenses
            ORDER BY id DESC
        """)

        expenses = cursor.fetchall()

        cursor.close()
        connection.close()

        return expenses

    def get_expense(self, expense_id):

        connection = self.connect()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, amount, category, description, date
            FROM expenses
            WHERE id = %s
        """, (expense_id,))

        expense = cursor.fetchone()

        cursor.close()
        connection.close()

        return expense

    def add_expense(
        self,
        amount,
        category,
        description,
        expense_date
    ):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO expenses
            (amount, category, description, date)
            VALUES (%s, %s, %s, %s)
        """, (
            amount,
            category,
            description,
            expense_date
        ))

        connection.commit()

        cursor.close()
        connection.close()

    def update_expense(
        self,
        expense_id,
        amount,
        category,
        description,
        expense_date
    ):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE expenses
            SET amount = %s,
                category = %s,
                description = %s,
                date = %s
            WHERE id = %s
        """, (
            amount,
            category,
            description,
            expense_date,
            expense_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

    def delete_expense(self, expense_id):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM expenses
            WHERE id = %s
        """, (expense_id,))

        connection.commit()

        cursor.close()
        connection.close()

    def search_expenses(self, search_term):

        connection = self.connect()

        cursor = connection.cursor(dictionary=True)

        search_pattern = f"%{search_term}%"

        cursor.execute("""
            SELECT id, amount, category, description, date
            FROM expenses
            WHERE category LIKE %s
               OR description LIKE %s
            ORDER BY id DESC
        """, (
            search_pattern,
            search_pattern
        ))

        expenses = cursor.fetchall()

        cursor.close()
        connection.close()

        return expenses

    def get_total(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM expenses
        """)

        total = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return total

    def get_category_totals(self):

        connection = self.connect()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                category,
                SUM(amount) AS total
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
        """)

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results