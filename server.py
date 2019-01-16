from flask import Flask, flash, redirect, render_template, request, session, abort
import database

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return render_template('page.html')
	elif request.method == 'POST':
		print(request.form['pubkey'])
		algo, pubkey, host = request.form['pubkey'].split(" ")
		database.insertKeys(host, pubkey, algo)
		return "Success"
	else:
		return "404"
 
if __name__ == "__main__":
	app.run(host='0.0.0.0')
