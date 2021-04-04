from models.budget import Budget
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo
import repositories.transaction_repository as transaction_repo
from datetime import datetime
from db.run_sql import run_sql

def select_all():
    sql = "SELECT * FROM budgets"
    results = run_sql(sql)
    budgets = []
    for row in results:
        budget = Budget(row['name'], row['start_date'], row['end_date'], row['amount'], row['id'])
        budgets.append(budget)
    return budgets

def save(budget):
    sql = "INSERT INTO budgets (name,start_date,end_date,amount) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [budget.name, budget.start_date, budget.end_date, budget.amount]
    result = run_sql(sql, values)[0]
    budget.id = result['id']
    return budget

def delete_all():
    sql = "DELETE FROM budgets"
    run_sql(sql)

def find_by_id(id):
    sql= "SELECT * FROM budgets WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    budget = Budget(result['name'], result['start_date'], result['end_date'], result['amount'], id)
    return budget

def delete(budget):
    sql = "DELETE FROM budgets WHERE id=%s"
    values = [budget.id]
    run_sql(sql, values)

def display(budget):
    pass
    #sql = "SELECT * FROM transactions WHERE"