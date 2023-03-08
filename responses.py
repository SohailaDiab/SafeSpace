from transformers import pipeline
classifier = pipeline('text-classification','unitary/toxic-bert')

def handle_response(text):
    score = classifier(text)[0]['score']

    if score>=0.5:
        return True
        
#text = "The weather is nice today, isn't it?"
#handle_response(text)