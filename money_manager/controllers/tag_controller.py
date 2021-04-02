from flask import Flask, render_template, redirect, request
from flask import Blueprint

import repositories.tag_repository as tag_repo

tags_blueprint = Blueprint("tags", __name__)