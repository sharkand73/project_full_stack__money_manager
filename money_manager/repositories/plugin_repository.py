import pdb
from db.run_sql import run_sql
from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction
from models.functions import convert_date

def save(transaction):
    sql = "INSERT INTO plugin_transactions (date,merchant_name,amount,tag_category) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [transaction.date, transaction.merchant.name, -transaction.amount, transaction.tag.category]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def delete_all():
    sql = "DELETE FROM plugin_transactions"
    run_sql(sql)

def select_all():
    sql = "SELECT * FROM plugin_transactions"
    results = run_sql(sql)
    transactions = []
    for row in results:
        merchant = Merchant(row['merchant_name'])
        tag = Tag(row['tag_category'])
        date = row['date']
        amount = row['amount']
        transaction = Transaction(date, merchant, amount, tag)
        transactions.append(transaction)
    return transactions


