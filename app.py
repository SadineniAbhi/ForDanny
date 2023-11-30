from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"

class OpenCloseForm(FlaskForm):
    submit_open = SubmitField("Open")
    submit_close = SubmitField("Close")

@app.route("/", methods=["GET", "POST"])
def home():
    form = OpenCloseForm()

    if form.validate_on_submit():
        if form.submit_open.data:
            print("Open")
        elif form.submit_close.data:
            print("Close")

    return render_template("home.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
