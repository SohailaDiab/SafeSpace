from transformers import pipeline

classifier = pipeline("zero-shot-classification", model = 'facebook/bart-large-mnli', multi_label=True, use_cdn=False)
labels = ["Bullying", "Natural", "discrimination"]

def handle_response(text):
    result = classifier(text, candidate_labels=labels)
    label = result['labels'][0]

    if result['scores'][0]>=0.5:
        if label not in ["Natural"]:
            return True
        