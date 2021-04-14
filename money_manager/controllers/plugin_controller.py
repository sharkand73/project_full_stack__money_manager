import pdb

from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.functions import file_list, validate, create_dict, convert_date_2
from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.plugin_repository as plugin_repo
import repositories.transaction_repository as transaction_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo 

plugins_blueprint = Blueprint("plugins", __name__)

@plugins_blueprint.route("/plugins")
def plugins():
    plugin_repo.delete_all()
    return render_template("/plugins/index.html")

@plugins_blueprint.route("/plugins/load", methods=["POST"])
def load():
    filename = request.form['filename']
    my_list = file_list(filename)               # OPEN filename
    result = validate(my_list)                  # If file is dodgy, return error web page
    if result == None:
        return ("This file is not in the correct format.")
    transactions_dict = create_dict(result)

    tag = Tag('Santander')
    transactions = []
    for trans_dict in transactions_dict:
        merchant = Merchant(trans_dict['description'])
        date = convert_date_2(trans_dict['date'])
        amount = trans_dict['amount']
        transaction = Transaction(date, merchant, amount, tag)
        plugin_repo.save(transaction)
        transactions.append(transaction)
    transactions.reverse()
    return render_template("/plugins/show.html", transactions = transactions, title = "Import Statement")

@plugins_blueprint.route("/plugins/save")
def save():
    transactions = plugin_repo.select_all()
    for transaction in transactions:
        merchant = merchant_repo.find_by_name(transaction.merchant.name)
        tag = tag_repo.find_by_category(transaction.tag.category)
        if merchant == None:
            merchant = transaction.merchant
            merchant_repo.save(merchant)
        if tag == None:
            tag = transaction.tag
            tag_repo.save(tag)
        new_transaction = Transaction(transaction.date, merchant, transaction.amount, tag)


        # merchants = merchant_repo.select_all()
        # merchant_names = [merchant.name for merchant in merchants]
        # tags = tag_repo.select_all()
        # tag_categories = [tag.category for tag in tags]
        # if transaction.tag.category not in tag_categories:
        #     tag_repo.save(transaction.tag)
        # if transaction.merchant.name not in merchant_names:
        #     merchant_repo.save(transaction.merchant)
        transaction_repo.save(new_transaction)
    plugin_repo.delete_all()
    return redirect("/transactions")

    ## If I can add extra optional description to tags, everything becomes easier