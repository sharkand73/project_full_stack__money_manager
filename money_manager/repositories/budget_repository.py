from models.budget import Budget
from models.transaction import Transaction
from models.spend import Spend
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
    sql_1 = "SELECT * FROM transctions" 
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

def spend_by_merchant(budget):
    sql_1 = "SELECT merchant_id,SUM(amount) FROM transactions"
    sql_2 = "INNER JOIN merchants ON transactions.merchant_id=merchants.id "
    sql_3 = "WHERE (date>=%s AND date<=%s) "
    sql_4 = "GROUP BY merchant_id "
    sql_5 = "ORDER BY sum(amount) DESC"
    sql = sql_1 + sql_2 + sql_3 + sql_4 + sql_5
    values = [budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d")]
    results = run_sql(sql, values)
    spends = []
    for row in results:
        merchant = merchant_repo.find_by_id(row['merchant_id'])
        spend = Spend(row['sum'], merchant = merchant)
        spends.append(spend)
    return spends

def spend_by_tag(budget):
    sql_1 = "SELECT tag_id,SUM(amount) FROM transactions"
    sql_2 = "INNER JOIN tags ON transactions.tag_id=tags.id "
    sql_3 = "WHERE (date>=%s AND date<=%s) "
    sql_4 = "GROUP BY tag_id "
    sql_5 = "ORDER BY sum(amount) DESC"
    sql = sql_1 + sql_2 + sql_3 + sql_4 + sql_5
    values = [budget.start_date.strftime("%Y-%m-%d"), budget.end_date.strftime("%Y-%m-%d")]
    results = run_sql(sql, values)
    spends = []
    for row in results:
        tag = tag_repo.find_by_id(row['tag_id'])
        spend = Spend(row['sum'], tag = tag)
        spends.append(spend)
    return spends
        
    
