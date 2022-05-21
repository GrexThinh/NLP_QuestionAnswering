from flask import Flask, render_template, request, url_for, redirect
from QA_1 import extractAnswer

app=Flask("app")

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method=="POST":
        question=request.form["question"]
        print(question)

        results, page, answer=extractAnswer(question)

        return render_template('home1.html', question=question, results=results, page=page, answer=answer)
    else:
        return render_template('home1.html', question="", results="", page="", answer="")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/home')
def home():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)