import streamlit as st
import os
import cv2
import numpy as np
from PIL import Image
import pytesseract
from pytesseract import Output
from ReadText import ReadText




def main():
    st.title("Image Text Processing")
    demo_image_path = "demo.png"  # Replace with the path to your demo image
    demo_image = Image.open(demo_image_path)
    use_demo_image = st.checkbox("Use Demo Image")

    if use_demo_image:
        img = demo_image
    else:
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            img = Image.open(uploaded_file)
        else:
            img = demo_image
    st.image(img, caption='Uploaded Image', use_column_width=True)

        # Create an instance of the ReadText class
    text_reader = ReadText(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))

        # Select operation
    selected_operation = st.selectbox("Select an operation", ['English Text', 'Find Text', 'Extract Numbers'])

    if selected_operation == 'English Text':
        english_text = text_reader.english()
        st.write(english_text)
    elif selected_operation == 'French Text':
        french_text = text_reader.french()
        st.write(french_text)
    elif selected_operation == 'Find Text':
        search_text = st.text_input("Enter the text to find")
        if st.button('Find'):
            found_text_image = text_reader.find(search_text)
            st.image(found_text_image, caption='Found Text', use_column_width=True)
    elif selected_operation == 'Extract Numbers':
        extracted_numbers = text_reader.number()
        st.write(extracted_numbers)
    elif selected_operation == 'Find Phone Numbers':
        phone_numbers = text_reader.phonenumber()
        if phone_numbers:
            st.write("Phone numbers found:",phone_numbers)
        else:
            st.write("No phone numbers found in the image.")
if __name__ == "__main__":
    main()
