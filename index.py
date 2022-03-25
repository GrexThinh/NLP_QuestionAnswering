from flask import Flask, render_template, request
from test import answerQuestionMachine

app=Flask("app")

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method=="POST":
        question=request.form["question"]
        ans=answerQuestionMachine(question)
        return render_template('index.html', content=ans)
    else:
        return render_template('index.html')

@app.route('/test')
def test():
    return "HELLO MY TEST!"

if __name__ == "__main__":
    app.run(debug=True)