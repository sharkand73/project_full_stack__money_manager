import pdb

from flask import Flask, render_template, redirect, request
from flask import Blueprint

import repositories.merchant_repository as merchant_repo
from models.merchant import Merchant
from repositories.transaction_repository import merchant_in_use


merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants_list = merchant_repo.select_all()
    for merchant in merchants_list:
        merchant.in_use = merchant_in_use(merchant)
    return render_template("/merchants/index.html", merchants = merchants_list, title = "View merchants")

@merchants_blueprint.route("/merchants/<id>/edit")
def edit(id):
    merchant = merchant_repo.find_by_id(id)
    return render_template("/merchants/edit.html", merchant = merchant, title = "Edit merchant" )

@merchants_blueprint.route("/merchants/<id>/update", methods=["POST"])
def update(id):
    merchant = merchant_repo.find_by_id(id)
    merchant.name = request.form['name']
    merchant_repo.update(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/delete", methods=["POST"])
def delete(id):
    merchant = merchant_repo.find_by_id(id)
    merchant_repo.delete(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/new")
def new():
    merchants = merchant_repo.select_all()
    return render_template("/merchants/new.html", title="New merchant", merchants=merchants)

@merchants_blueprint.route("/merchants", methods=["POST"])
def save():
    merchants = merchant_repo.select_all()              # GET A LIST OF ALL MERCHANTS FROM THE DB TABLE
    names = [merchant.name for merchant in merchants]   # MAKE A LIST OF MERCHANT NAMES OUT OF THIS LIST
    new_name = request.form['name']                     # TAKE THE USER'S INPUT (A MERCHANT NAME)
    new_merchant = Merchant(new_name)                   # CREATE A NEW MERCHANT OBJECT OUT OF IT
    if new_name and (new_name not in names):            # CHECK NAME IS NOT EMPTY
                                                        # CHECK NAME IS NOT IN USE
        merchant_repo.save(new_merchant)                # SAVE NEW MERCHANT TO DATABASE             
    return redirect("/merchants")                       # RETURN TO "SHOW MERCHANTS"