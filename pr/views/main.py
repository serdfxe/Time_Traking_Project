from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from pr.config import *


main = Blueprint("main", __name__)


@main.route("/<s>", methods=('GET', 'POST'))
def root_page(s):
    return render_template("another.html", side_bar_components=side_bar_components, side_bar_logos=side_bar_logos, current=s, content=content[s])


@main.route("/", methods=('GET', 'POST'))
def empty_page():
    return redirect(url_for("main.root_page", s="main"))
