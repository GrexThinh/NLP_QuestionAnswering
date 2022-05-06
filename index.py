from flask import Flask, render_template, request, url_for, redirect
from QA import answerQuestionMachine

app=Flask("app")

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method=="POST":
        question=request.form["question"]
        answer, context=answerQuestionMachine(question)
        return render_template('home.html', ans=answer, ques=question, context=context)
    else:
        return render_template('home.html', ans = "", context = "")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/home')
def home():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)