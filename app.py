import streamlit as st

st.title("Plant Disease Detection System 🌿")

st.write("Welcome to the Plant Disease Detection System!")

st.markdown("""
### About This App
This is a machine learning application that can detect plant diseases from images.

### Features
- Upload plant images
- Get disease predictions
- User-friendly interface

### Status
🚧 **Currently in deployment test mode** 🚧

The full functionality with the trained model will be available once deployment is confirmed.

### How to Use
1. Upload an image of a plant leaf
2. Click predict
3. Get the disease prediction

**Note: This is a test deployment to ensure the hosting platform works correctly.**
""")

# Simple file uploader
uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Predict'):
        st.success("✅ Deployment successful! This is a test prediction.")
        st.info("Full model functionality will be added once deployment is confirmed.")
        st.write("**Predicted Disease:** Healthy Plant (Test Mode)") 