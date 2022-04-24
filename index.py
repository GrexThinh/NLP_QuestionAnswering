from flask import Flask, render_template, request, url_for, redirect
from test import answerQuestionMachine

app=Flask("app")

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method=="POST":
        question=request.form["question"]
        ans=answerQuestionMachine(question)
        return render_template('index1.html', content=ans)
    else:
        return render_template('index1.html',content = "Hello World", content1 = "Goodbye")

@app.route('/about')
def about():
    return "THÔNG TIN NHÓM"

@app.route('/home')
def home():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)