from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")
labels = ["bullying", "toxic", "neutral"]

def classify_image(image_array):
    """
    This function takes an image array and enters it to the clip vit transformer
    True if the image has bullying, toxic content or something like that
    
    Parameters:
    - image_array: np.array
    
    Returns: 
    - label
    """
    inputs = processor(text=labels, images=image_array, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
    label_idx = probs.argmax().item() # take the category with the highest probability 
    label =  labels[label_idx]

    if label != 'neutral':
        return True

