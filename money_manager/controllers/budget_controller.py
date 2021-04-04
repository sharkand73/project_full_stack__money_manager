import pdb
from flask import Flask, render_template, redirect, request
from flask import Blueprint

#import repositories.tag_repository as tag_repo
#import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo
import repositories.budget_repository as budget_repo
#from models.transaction import Transaction
from models.budget import Budget

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
    return render_template("budgets/view.html", budget = budget, spend = spend, transaction = transactions, title = "View Budget")
    

@budgets_blueprint.route("/budgets/new")
def new():
    pass

@budgets_blueprint.route("/budgets", methods=["POST"])
def save():
    pass

@budgets_blueprint.route("/budgets/<id>/edit")
def edit():
    pass

@budgets_blueprint.route("/budgets/<id>", methods = ["POST"])
def update():
    pass

@budgets_blueprint.route("/budgets/<id>/delete", methods = ["POST"])
def delete(id):
    budget = budget_repo.find_by_id(id)
    budget_repo.delete(budget)
    return redirect("/budgets")

        
