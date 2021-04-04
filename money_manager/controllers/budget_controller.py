import pdb
from flask import Flask, render_template, redirect, request
from flask import Blueprint

#import repositories.tag_repository as tag_repo
#import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo
import repositories.budget_repository as budget_repo
#from models.transaction import Transaction
from models.budget import Budget
from models.functions import convert_date

budgets_blueprint = Blueprint("budgets", __name__)

@budgets_blueprint.route("/budgets")
def budgets():
    budgets = budget_repo.select_all()
    for budget in budgets:
        colors = ['blue', 'red']
        spend = budget_repo.spend(budget)
        budget.color = colors[(spend > budget.amount)]
    return render_template("/budgets/index.html", budgets = budgets, title = "All Budgets")

@budgets_blueprint.route("/budgets/<id>")
def show(id):
    budget = budget_repo.find_by_id(id)
    transactions = budget_repo.display(budget)
    spend = budget_repo.spend(budget)
    colors = ['blue', 'red']
    budget.color = colors[(spend > budget.amount)]
    return render_template("budgets/view.html", budget = budget, spend = spend, transactions = transactions, title = "View Budget")
    

@budgets_blueprint.route("/budgets/new", methods = ["POST"])
def new():
    budgets = budget_repo.select_all()
    for budget in budgets:
        colors = ['blue', 'red']
        spend = budget_repo.spend(budget)
        budget.color = colors[(spend > budget.amount)]
    return render_template("/budgets/new.html", budgets = budgets, title = "New Budget")

@budgets_blueprint.route("/budgets", methods=["POST"])
def save():
    name = request.form['name']
    start_string = request.form['start_date']
    end_string = request.form['end_date']
    start_date = convert_date(start_string)
    end_date = convert_date(end_string)
    amount = request.form['amount']
    budget = Budget(name, start_date, end_date, amount)
    budget_repo.save(budget)
    return redirect("/budgets")

@budgets_blueprint.route("/budgets/<id>/edit", methods=["POST"])
def edit(id):
    budget = budget_repo.find_by_id(id)
    return render_template("budgets/edit.html", budget = budget, title = "Edit Budget")

@budgets_blueprint.route("/budgets/<id>", methods = ["POST"])
def update(id):
    name = request.form['name']
    start_string = request.form['start_date']
    end_string = request.form['end_date']
    start_date = convert_date(start_string)
    end_date = convert_date(end_string)
    amount = request.form['amount']
    budget = Budget(name, start_date, end_date, amount, id)
    budget_repo.update(budget)
    return redirect("/budgets")
    

@budgets_blueprint.route("/budgets/<id>/delete", methods = ["POST"])
def delete(id):
    budget = budget_repo.find_by_id(id)
    budget_repo.delete(budget)
    return redirect("/budgets")

        
