from flask import Flask, render_template, redirect, request
from flask import Blueprint

import repositories.merchant_repository as merchant_repo

merchants_blueprint = Blueprint("merchants", __name__)