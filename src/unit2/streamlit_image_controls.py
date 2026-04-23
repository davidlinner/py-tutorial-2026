import streamlit as st
import numpy as np
import cv2

st.title("Image Playground")
size = st.slider("Image size", 100, 400, 220)
blur_strength = st.slider("Blur strength", 1, 21, 9, step=2)
show_edges = st.checkbox("Show edges", value=False)

image = np.zeros((size, size, 3), dtype=np.uint8)
cv2.circle(image, (size // 2, size // 2), size // 4, (0, 180, 255), -1)
cv2.rectangle(image, (20, 20), (size - 20, size - 20), (255, 255, 255), 2)

blurred = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)
st.image(blurred, channels="BGR", caption="Blurred synthetic image")

if show_edges:
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 160)
    st.image(edges, caption="Detected edges")
