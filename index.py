from flask import Flask, render_template, request
from test import answerQuestionMachine

app=Flask("app")

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method=="POST":
        question=request.form["question"]
        print(question)
        answer=answerQuestionMachine(question)
        return render_template('index.html', ques=question, ans=answer)
    else:
        return render_template('index.html')

@app.route('/about')
def about():
    return "THÔNG TIN NHÓM"

if __name__ == "__main__":
    app.run(debug=True)