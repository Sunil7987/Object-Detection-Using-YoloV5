from pathlib import Path
import streamlit as st
import cv2
import torch
from PIL import Image
import numpy as np


model = torch.hub.load('ultralytics/yolov5', 'custom', path="best.pt")  # load scratch


   
def detect_main():
    """Fruit Object Detection APP"""

    st.title("Fruit Object Detection")

    choice = st.radio("", ("Show Demo", "Browse an Image"))
    st.write()

    if choice == "Browse an Image":
        st.set_option('deprecation.showfileUploaderEncoding', False)
        image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

        if image_file is not None:
            our_image = Image.open(image_file) 
            img  = model(our_image)
            st.image(np.squeeze(img.render())) 
            

    elif choice == "Show Demo":
        our_image = Image.open(r"C:\Users\HP\Desktop\Object_Detection_Streamlit\YoloV5_Fruits_Detection\oranges-apple-banana-260nw-637509382.jpg")
        img = model(our_image)
        st.image(np.squeeze(img.render()))

if __name__ == '__main__':
    detect_main()