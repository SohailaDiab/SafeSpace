from transformers import pipeline
classifier = pipeline('text-classification','unitary/toxic-bert')

def handle_response(text):
    """
    This function takes text message and classifiy it using toxic bert transformer
    return : True if the text is bullying, toxic or something like that
    """
    score = classifier(text)[0]['score']

    if score>=0.5:
        return True
        