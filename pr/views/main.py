from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from pr.config import *


main = Blueprint("main", __name__)


@main.route("/<s>", methods=('GET', 'POST'))
def root_page(s):
    return render_template(urls_to_files[s], side_bar_components=side_bar_components, side_bar_logos=side_bar_logos, current=s)


@main.route("/", methods=('GET', 'POST'))
def empty_page():
    return redirect(url_for("root_page", s="main"))
