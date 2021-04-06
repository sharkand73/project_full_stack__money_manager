import pdb

from models.testimonial import Testimonial
from random import choice
from db.run_sql import run_sql

def select_random():
    sql = "SELECT * FROM testimonials"
    results = run_sql(sql)
    testimonials = []
    for row in results:
        testimonial = Testimonial(row[1], row[2])
        testimonials.append(testimonial)
    return choice(testimonials)