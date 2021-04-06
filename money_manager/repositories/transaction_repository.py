from models.transaction import Transaction
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

from db.run_sql import run_sql

def process(results):   # handy wee function to avoid repetition in the various "select_all" methods
    transactions = []
    for row in results:
        date = row['date']
        merchant = merchant_repo.find_by_id(row['merchant_id'])
        amount = row['amount']
        tag = tag_repo.find_by_id(row['tag_id'])
        id = row['id']
        transaction = Transaction(date, merchant, amount, tag, id)
        transactions.append(transaction)
    return transactions


def select_all():  #selects all transactions, ordering them by date
    sql = "SELECT * FROM transactions ORDER BY date"
    results = run_sql(sql)
    return process(results)

def order_by_merchant():   #selects all transactions, ordering them by merchant name
    sql_1 = "SELECT * FROM transactions "
    sql_2 = "INNER JOIN merchants ON transactions.merchant_id = merchants.id " 
    sql_3 = "ORDER BY merchants.name"
    results = run_sql(sql_1 + sql_2 + sql_3)
    return process(results)

def order_by_tag(): #selects all transactions, ordering them by tag category
    sql_1 = "SELECT * FROM transactions "
    sql_2 = "INNER JOIN tags ON transactions.tag_id = tags.id " 
    sql_3 = "ORDER BY tags.category"
    results = run_sql(sql_1 + sql_2 + sql_3)
    return process(results)

def save(transaction):
    sql = "INSERT INTO transactions (date,merchant_id,amount,tag_id) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [transaction.date, transaction.merchant.id, transaction.amount, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def find_by_id(id):
    sql = "SELECT * FROM transactions WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result != None:
        date = result['date']
        merchant = merchant_repo.find_by_id(result['merchant_id'])
        amount = result['amount']
        tag = tag_repo.find_by_id(result['tag_id'])
        transaction = Transaction(date, merchant, amount, tag, id)
        return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(transaction):
    sql = "DELETE FROM transactions WHERE id=%s"
    values = [transaction.id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET ( date, merchant_id, amount, tag_id ) = ( %s,%s,%s,%s ) WHERE id=%s"
    values = [transaction.date, transaction.merchant.id, transaction.amount, transaction.tag.id, transaction.id]
    run_sql(sql, values)

def sum():
    sql = "SELECT SUM(amount) FROM transactions"
    total = run_sql(sql)
    return total

