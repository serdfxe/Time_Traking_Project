from flask import Flask, redirect, render_template, url_for


app = Flask(__name__)

urls_to_files = {
    "main": "main_page.html",
    "page_two": "page_two.html"
}


@app.route("/<s>", methods=('GET', 'POST'))
def root_page(s):
    return render_template(urls_to_files[s])



@app.route("/", methods=('GET', 'POST'))
def empty_page():
    return redirect(url_for("root_page", s="main"))

app.run("0.0.0.0", port="80", debug=True)
