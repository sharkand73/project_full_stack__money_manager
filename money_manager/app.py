from flask import Flask, render_template, redirect, request
from flask import Blueprint

from controllers.tag_controller import tags_blueprint
from controllers.merchant_controller import merchants_blueprint
from controllers.transaction_controller import transactions_blueprint
from controllers.budget_controller import budgets_blueprint
from controllers.plugin_controller import plugins_blueprint

from repositories.testimonial_repository import select_random

app = Flask(__name__)

app.register_blueprint(tags_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(budgets_blueprint)
app.register_blueprint(plugins_blueprint)


@app.route("/")
def home():
    testimonial = select_random()
    return render_template("/index.html", title="home", testimonial = testimonial)

if __name__ == "__main__":
    app.run(debug=True)