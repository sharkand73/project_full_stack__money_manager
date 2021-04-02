import pdb

from flask import Flask, render_template, redirect, request
from flask import Blueprint

import repositories.tag_repository as tag_repo

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repo.select_all()
    return render_template("/tags/index.html", tags = tags, title = "Numus: View Tags")

@tags_blueprint.route("/tags/<id>/edit", methods=["POST"])
def edit(id):
    tag = tag_repo.find_by_id(id)
    return render_template("/tags/edit.html", tag = tag, title = "Numus: Edit Tag" )

@tags_blueprint.route("/tags/<id>/update", methods=["POST"])
def update(id):
    tag = tag_repo.find_by_id(id)
    tag.category = request.form['category']
    tag_repo.update(tag)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/delete", methods=["POST"])
def delete(id):
    tag = tag_repo.find_by_id(id)
    tag_repo.delete(tag)
    return redirect("/tags")