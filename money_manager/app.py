from flask import Flask, render_template, redirect, request
from flask import Blueprint

from controllers.tag_controller import tags_blueprint
from controllers.merchant_controller import merchants_blueprint
from controllers.transaction_controller import transactions_blueprint
from controllers.budget_controller import budgets_blueprint

app = Flask(__name__)

app.register_blueprint(tags_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(budgets_blueprint)


@app.route("/")
def home():
    return render_template("/index.html", title="home")

if __name__ == "__main__":
    app.run(debug=True)