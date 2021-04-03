import pdb

from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repo

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repo.select_all()
    return render_template("/tags/index.html", tags = tags, title = "View Tags")

@tags_blueprint.route("/tags/<id>/edit", methods=["POST"])
def edit(id):
    tag = tag_repo.find_by_id(id)
    return render_template("/tags/edit.html", tag = tag, title = "Edit Tag" )

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

@tags_blueprint.route("/tags/new", methods=["POST"])
def new():
    tags = tag_repo.select_all()
    return render_template("/tags/new.html", title="New Tag", tags=tags)

@tags_blueprint.route("/tags", methods=["POST"])
def save():
    tags = tag_repo.select_all()
    categories = [tag.category for tag in tags]
    new_category = request.form['category']
    new_tag = Tag(new_category)
    if new_category and (new_category not in categories):
        tag_repo.save(new_tag)
    return redirect("/tags")