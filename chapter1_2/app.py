import gradio as gr
from fastai.vision.all import *
import skimage

learn = load_learner('chapter1_2\models\dog_breed_classifier.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

title = "Pet Breed Classifier"
description = "A dog breed classifier trained with fastai. Trained on self-collected images of 'Bulldog', 'Chihuahua', 'Dachshund', 'Dalmatian', 'Golden Retriever', 'Poodle', 'Pug', 'Siberian Husky' Created as a demo for Gradio and HuggingFace Spaces."
article="<p style='text-align: center'><a href='https://tmabraham.github.io/blog/gradio_hf_spaces_tutorial' target='_blank'>Blog post</a></p>"
examples = ['data/chihuahua.jpg']
interpretation='default'
enable_queue=True

gr.Interface(fn=predict,inputs=gr.inputs.Image(shape=(512, 512)),outputs=gr.outputs.Label(num_top_classes=3),title=title,description=description,article=article,examples=examples,interpretation=interpretation,enable_queue=enable_queue).launch()