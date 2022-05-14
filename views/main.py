from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from Time_Traking_Project.config import *


main = Blueprint("main", __name__)


@main.route("/<s>", methods=('GET', 'POST'))
def root_page(s):
    return render_template(urls_to_files[s], side_bar_components=side_bar_components, current=s)


@main.route("/", methods=('GET', 'POST'))
def empty_page():
    return redirect(url_for("root_page", s="main"))
