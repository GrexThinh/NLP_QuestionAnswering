from flask import Flask, render_template, request, url_for, redirect
from QA import answerQuestionMachine, DocumentRetrieval, QueryProcessor, PassageRetrieval, AnswerExtractor

import concurrent.futures
import itertools
import operator
import re
import os
import spacy

import requests
import wikipedia
from gensim.summarization.bm25 import BM25
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, QuestionAnsweringPipeline

SPACY_MODEL = os.environ.get('SPACY_MODEL', 'en_core_web_sm')
QA_MODEL = os.environ.get('QA_MODEL', 'distilbert-base-cased-distilled-squad')
nlp = spacy.load(SPACY_MODEL, disable=['ner', 'parser', 'textcat'])
query_processor = QueryProcessor(nlp)
document_retriever = DocumentRetrieval()
passage_retriever = PassageRetrieval(nlp)
answer_extractor = AnswerExtractor(QA_MODEL, QA_MODEL)

app=Flask("app")

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method=="POST":
        question=request.form["question"]
        """
        answer, context=answerQuestionMachine(question)"""
        query = query_processor.generate_query(question)
        docs = document_retriever.search(query)
        passage_retriever.fit(docs)
        passages = passage_retriever.most_similar(question)
        answers = answer_extractor.extract(question, passages)

        return render_template('home.html', ans=answers[0], ques=question)
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