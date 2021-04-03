from models.transaction import Transaction
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

from db.run_sql import run_sql

def save(transaction):
    sql = "INSERT INTO transactions ( merchant_id,amount,tag_id ) VALUES ( %s,%s,%s ) RETURNING id"
    values = [transaction.merchant.id, transaction.amount, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    transactions = []
    for row in results:
        merchant = merchant_repo.find_by_id(row['merchant_id'])
        amount = row['amount']
        tag = tag_repo.find_by_id(row['tag_id'])
        id = row['id']
        transaction = Transaction(merchant, amount, tag, id)
        transactions.append(transaction)
    return transactions

def find_by_id(id):
    sql = "SELECT * FROM transactions WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result != None:
        merchant = merchant_repo.find_by_id(result['merchant_id'])
        amount = result['amount']
        tag = tag_repo.find_by_id(result['tag_id'])
        transaction = Transaction(merchant, amount, tag, id)
        return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(transaction):
    sql = "DELETE FROM transactions WHERE id=%s"
    values = [transaction.id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET ( merchant_id, amount, tag_id ) = ( %s,%s,%s ) WHERE id=%s"
    values = [transaction.merchant.id, transaction.amount, transaction.tag.id, transaction.id]
    run_sql(sql, values)
