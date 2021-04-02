from flask import Flask, render_template, redirect, request
from flask import Blueprint

import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo

transactions_blueprint = Blueprint("transactions", __name__)