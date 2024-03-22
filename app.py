import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import streamlit as st

from PIL import Image

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))


def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(
        [
            input,
            image,
            prompt
        ]
    )
    return response.text

# def input_image_setup(uploaded_file):
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type":uploaded_file.type,
#                 "data":bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         return FileNotFoundError("No file uploaded")
    


## Initializing our streamlit app
st.set_page_config(page_title = "Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key = "input")
uploaded_file=st.file_uploader("Choose an image: ", type=["jpg", "jpeg", "png", "image/png"])


image = ""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the Animal Image")

input_prompt = """
    You are an expert in detecting and identifying the animals images. 
    You will receive input images which contains animals and you will have to answer the 
    questions based on input image
"""

## if submit button is clicked
if submit:
    #image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(
        input_prompt,
        image,
        input
    )

    st.subheader("The Response is : ")
    st.write(response)



