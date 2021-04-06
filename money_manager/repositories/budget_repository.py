from models.budget import Budget
from models.transaction import Transaction
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
    values = [budget.name, budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d"), budget.amount]
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

def update(budget):
    sql = "UPDATE budgets SET ( name,start_date,end_date,amount )=( %s,%s,%s,%s ) WHERE id=%s"
    values = [budget.name, budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d"), budget.amount, budget.id]
    run_sql(sql, values)

def display(budget):
    sql = "SELECT * FROM transactions WHERE (date>=%s AND date<=%s)"
    values = [budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d")]
    results = run_sql(sql, values)
    return transaction_repo.process(results)

def display_by_merchant(budget):
    sql_1 = "SLECT * FROM transctions" 
    sql_2 = "INNER JOIN merchants ON transactions.merchant_id = merchants.id "
    sql_3 = "ORDER BY merchants.name "
    sql_4 = "WHERE (date>=%s AND date<=%s)"
    sql = sql_1 + sql_2 + sql_3 + sql_4
    values = [budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d")]
    results = run_sql(sql, values)
    return transaction_repo.process(results)

def display_by_tag(budget):
    sql_1 = "SLECT * FROM transctions" 
    sql_2 = "INNER JOIN tags ON transactions.tag_id = tags.id "
    sql_3 = "ORDER BY tags.category "
    sql_4 = "WHERE (date>=%s AND date<=%s)"
    sql = sql_1 + sql_2 + sql_3 + sql_4
    values = [budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d")]
    results = run_sql(sql, values)
    return transaction_repo.process(results)

def spend(budget):
    sql = "SELECT SUM(amount) FROM transactions WHERE (date>=%s AND date<=%s)"
    values = [budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d")]
    spend = run_sql(sql, values)[0][0]
    if spend == None:
        spend = 0
    return spend