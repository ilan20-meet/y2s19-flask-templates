from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	foods = ["steak", "sushi", "burrito"]
	return render_template("index.html", foods=foods, no_foods=False)

if __name__ == '__main__':
   app.run(debug = True)
