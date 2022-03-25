

# question = "What is machine learning?"

# import torch

# from transformers import BertForQuestionAnswering

# model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')

# from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')

# tokenizer.encode(question, truncation=True, padding=True)

# from transformers import pipeline




def answerQuestionMachine(question):
    context = """" 
    Machine learning (ML) is the study of computer algorithms that improve automatically through experience. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as email filtering and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.
    """
    from transformers import pipeline
    model_name = "deepset/bert-base-cased-squad2"

    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)
    return res["answer"]

