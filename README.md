# Image2Text
This streamlit app Takes an image as input as an image, reads the text using pytesseract, and displays it on the webpage. This also has some additional features like detecting numbers, Finding given text.

# Features

1. Image Text Extraction: Users can upload an image containing text, and the app will leverage pytesseract to extract the text from the image. The extracted text is then displayed on the webpage for easy viewing and analysis.

2. Number Detection: The app can also detect and extract numerical values present within the image. It recognizes various formats of numbers, including phone numbers and numeric sequences.

3. Text Search: Users can input specific text they want to find within the image. The app will scan the image and highlight any occurrences of the provided text, making it easy to locate and identify relevant information.

# How it Works

1. Uploading the Image: Users can simply upload an image through the user interface of the app. The app accepts images in various formats, such as JPEG, PNG, etc.

2. Text Extraction: Upon image upload, the app utilizes pytesseract, a Python library for Optical Character Recognition (OCR), to extract the text present in the image. The extracted text is then displayed on the webpage for easy reading.

3. Number Detection: The app processes the extracted text to identify and extract numerical values like phone numbers and other numeric sequences.

4. Text Search: If users provide a specific text to search for, the app scans the extracted text to find and highlight occurrences of the provided text.

# Technologies Used

Streamlit: For creating the user interface and deploying the app quickly.
Pytesseract: For Optical Character Recognition (OCR) to extract text from images.
OpenCV: For image processing and manipulation, if required.
Python: The primary programming language used for building the application.

Try It Out!
I welcome you to check out this Streamlit OCR app and experience the seamless text extraction and other additional features it offers. Feel free to provide feedback, suggestions, and bug reports to help me improve the app and make it more useful for everyone.

Link to the GitHub repository: https://image2text-sl3vxn6fdh.streamlit.app/

Thank you for your time, and happy text extraction with Streamlit OCR App! 🚀
