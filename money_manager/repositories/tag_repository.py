from models.tag import Tag
from db.run_sql import run_sql

def save(tag):
    sql = "INSERT INTO tags ( category ) VALUES ( %s ) RETURNING id"
    values = [tag.category]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    sql = "SELECT * FROM tags ORDER BY category"
    results = run_sql(sql)
    tags = []
    for row in results:
        tag = Tag(row['category'], row['id'])
        tags.append(tag)
    return tags

def find_by_id(id):
    sql = "SELECT * FROM tags WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result != None:
        tag = Tag(result['category'], id)
        return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def update(tag):
    sql = "UPDATE tags SET category=%s WHERE id=%s"
    values = [tag.category, tag.id]
    run_sql(sql, values)

def delete(tag):
    if len(select_all())>1:
        sql = "DELETE FROM tags WHERE id=%s"
        values = [tag.id]
        run_sql(sql, values)

def find_by_category(tag_category):
    sql = "SELECT * FROM tags WHERE category=%s"
    values = [tag_category]
    results = run_sql(sql, values)
    if results:
        tag = Tag(tag_category, results[0]['id'])
        return tag

    
