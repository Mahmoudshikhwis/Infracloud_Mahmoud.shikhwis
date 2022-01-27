"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, flash, request, redirect, session,logging,request




app = Flask(__name__)



@app.route("/")
def index():
    return "welcome to the index page"


@app.route("/hi/")
def who():
    return"who are you?"




if __name__ == '__main__':
	app.debug = True
	app.secret_key = "124"
	app.run(host='127.0.0.1')
