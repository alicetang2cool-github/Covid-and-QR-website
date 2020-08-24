from flask import Flask, render_template, url_for, redirect
from forms import StringForm, PasswordForm
import pyqrcode, getpass
from pyqrcode import QRCode 
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = "Home")

@app.route("/about")    
def about():
    return render_template('about.html', title = "About")

@app.route("/make")    
def make():
    return render_template('make.html', title = "Maker")

@app.route("/makeStringQRcode", methods=['GET', 'POST']) 
def makeStringQRcode():
    form = StringForm()
    if form.validate_on_submit():
        s = str(form.string.data)
        QR = pyqrcode.create(s)
        myfile = os.path.join(app.static_folder, "QR.png")
        QR.png(myfile, scale = 5) 
        return redirect(url_for('QRcodedisplay'))
    return render_template('makeStringQRcode.html', title = 'Maker', form=form)

@app.route("/makePasswordQRcode", methods=['GET', 'POST']) 
def makePasswordQRcode():
    form = PasswordForm()
    if form.validate_on_submit():
        s = str(form.password.data)
        QR = pyqrcode.create(s)
        myfile = os.path.join(app.static_folder, "QR.png")
        QR.png(myfile, scale = 5) 
        return redirect(url_for('QRcodedisplay'))
    return render_template('makePasswordQRcode.html', title = 'Maker', form=form)

@app.route("/QRcodedisplay") 
def QRcodedisplay():
    return render_template('QRcodedisplay.html', title = "Maker")

if __name__ == '__main__':
    app.run(debug=True)
