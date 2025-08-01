import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("🌄 Image Noise Removal Filters")

uploaded_file = st.file_uploader("📤 Upload a grayscale image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")  
    img_array = np.array(image)


    # Apply filters
    avg = cv2.blur(img_array, (5, 5))
    gaussian = cv2.GaussianBlur(img_array, (5, 5), 0)
    median = cv2.medianBlur(img_array, 5)
    bilateral = cv2.bilateralFilter(img_array, 9, 75, 75)

    
    avg_pil = Image.fromarray(avg)
    gaussian_pil = Image.fromarray(gaussian)
    median_pil = Image.fromarray(median)
    bilateral_pil = Image.fromarray(bilateral)

    # Show original
    st.subheader("🖼️ Original Image")
    st.image(image, caption="Original", use_container_width=True
)

    
    st.subheader("✨ Filtered Results")

    col1, col2 = st.columns(2)
    with col1:
        st.image(avg_pil, caption="Averaging", use_container_width=True
)
    with col2:
        st.image(gaussian_pil, caption="Gaussian", use_container_width=True
)

    col3, col4 = st.columns(2)
    with col3:
        st.image(median_pil, caption="Median", use_container_width=True
)
    with col4:
        st.image(bilateral_pil, caption="Bilateral", use_container_width=True
)
