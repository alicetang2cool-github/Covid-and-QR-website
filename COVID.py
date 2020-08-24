from flask import Flask, render_template, url_for, flash, redirect, session, send_file
from forms import StateForm
import pickle
import makeimage

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/PickAState", methods=['GET', 'POST'])
def PickAState():
    form = StateForm()
    if form.validate_on_submit():
        s = form.States.data
        session['state'] = s
        return redirect(url_for('map'))
    return render_template('PickAState.html', form=form)

@app.route("/map",methods=['GET', 'POST'])
def map():
    return render_template('map.html')

@app.route("/getCases")
def getCases():
    filePath = "./imageOfCases/" + session['state'] + ".png"
    return send_file(filePath, mimetype = 'image/png')

@app.route("/getDeaths")
def getDeaths():
    filePath = "./imageOfDeaths/" + session['state'] + ".png"
    return send_file(filePath, mimetype = 'image/png')

if __name__ == '__main__':
    app.run(debug=True)

