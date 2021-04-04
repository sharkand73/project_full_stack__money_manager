import pdb
from flask import Flask, render_template, redirect, request
from flask import Blueprint

import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo
from models.transaction import Transaction

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transaction_list = transaction_repo.select_all()
    total = transaction_repo.sum()[0][0]
    return render_template("/transactions/index.html", total = total, transactions = transaction_list, title = "View Transactions")

@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete(id):
    transaction = transaction_repo.find_by_id(id)
    transaction_repo.delete(transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/new", methods=["POST"])
def new():
    tags = tag_repo.select_all()
    merchants = merchant_repo.select_all()
    transactions = transaction_repo.select_all()
    return render_template("/transactions/new.html", tags = tags, merchants = merchants, transactions = transactions, title = "New Transaction")

@transactions_blueprint.route("/transactions", methods=["POST"])
def save():
    date = request.form['date']
    merchant = merchant_repo.find_by_id(request.form['merchant_id'])
    amount = request.form['amount']
    tag= tag_repo.find_by_id(request.form['tag_id'])
    new_transaction = Transaction(date, merchant, amount, tag)
    transaction_repo.save(new_transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/edit", methods=["POST"])
def edit(id):
    transaction = transaction_repo.find_by_id(id)
    tags = tag_repo.select_all()
    merchants = merchant_repo.select_all()
    return render_template("/transactions/edit.html", transaction = transaction, merchants = merchants, tags = tags, title = "Edit Transaction")

@transactions_blueprint.route("/transactions/<id>/update", methods=["POST"])
def update(id):
    date = request.form['date']
    merchant = merchant_repo.find_by_id(request.form['merchant_id'])
    amount = request.form['amount']
    tag = tag_repo.find_by_id(request.form['tag_id'])
    transaction = Transaction(date, merchant, amount, tag, id)
    transaction_repo.update(transaction)
    return redirect("/transactions")