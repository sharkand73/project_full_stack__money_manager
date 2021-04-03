from flask import Flask, render_template, redirect, request
from flask import Blueprint

import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transaction_list = transaction_repo.select_all()
    return render_template("/transactions/index.html", transactions = transaction_list, title = "View Transactions")

@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete(id):
    transaction = transaction_repo.find_by_id(id)
    if len(transaction_repo.select_all()) > 1:
        transaction_repo.delete(transaction)
    return redirect("/transactions")

