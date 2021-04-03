from models.merchant import Merchant
from db.run_sql import run_sql

def save(merchant):
    sql = "INSERT INTO merchants ( name ) VALUES ( %s ) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    merchants = []
    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

def find_by_id(id):
    sql = "SELECT * FROM merchants WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result != None:
        merchant = Merchant(result['name'], id)
        return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def update(merchant):
    sql = "UPDATE merchants SET name=%s WHERE id=%s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)

def delete(merchant):
    if len(select_all())>1:
        sql = "DELETE FROM merchants WHERE id=%s"
        values = [merchant.id]
        run_sql(sql, values)
    
