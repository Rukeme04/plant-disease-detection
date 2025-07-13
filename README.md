# Plant Disease Detection System 🌿🔍

A machine learning-based web application that can identify plant diseases from images using deep learning techniques.

## 🌟 Features

- **Real-time Disease Detection**: Upload plant images and get instant disease predictions
- **38 Disease Categories**: Supports detection of diseases in various crops including:
  - Apple (Apple scab, Black rot, Cedar apple rust, Healthy)
  - Blueberry (Healthy)
  - Cherry (Powdery mildew, Healthy)
  - Corn/Maize (Cercospora leaf spot, Common rust, Northern Leaf Blight, Healthy)
  - Grape (Black rot, Esca, Leaf blight, Healthy)
  - Orange (Citrus greening)
  - Peach (Bacterial spot, Healthy)
  - Pepper (Bacterial spot, Healthy)
  - Potato (Early blight, Late blight, Healthy)
  - Raspberry (Healthy)
  - Soybean (Healthy)
  - Squash (Powdery mildew)
  - Strawberry (Leaf scorch, Healthy)
  - Tomato (Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, Spider mites, Target Spot, Yellow Leaf Curl Virus, Mosaic virus, Healthy)

- **User-Friendly Interface**: Simple and intuitive Streamlit web interface
- **High Accuracy**: State-of-the-art deep learning model for reliable predictions

## 🚀 Live Demo

[Link will be available after deployment]

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: TensorFlow/Keras
- **Image Processing**: OpenCV, PIL
- **Data Processing**: NumPy, Pandas

## 📊 Dataset

The model is trained on a comprehensive dataset containing:
- **87K+ RGB images** of healthy and diseased crop leaves
- **38 different classes** of plant diseases
- **80/20 training-validation split**
- **33 test images** for evaluation

## 🏃‍♂️ Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Plant_Disease_Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

### Using Anaconda

1. **Create and activate environment**
   ```bash
   conda create -n plant_disease python=3.9
   conda activate plant_disease
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 📁 Project Structure

```
Plant_Disease_Prediction/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── trained_model.h5       # Trained model (H5 format)
├── trained_model.keras    # Trained model (Keras format)
├── home_page.jpeg         # Home page image
├── test_model.py          # Model testing script
└── Plant_Disease_Dataset/ # Dataset directory
```

## 🎯 How to Use

1. **Navigate to Disease Recognition**: Click on "Disease Recognition" in the sidebar
2. **Upload Image**: Choose an image of a plant leaf you want to analyze
3. **Preview**: Click "Show Image" to preview the uploaded image
4. **Predict**: Click "Predict" to get the disease prediction
5. **View Results**: The system will display the predicted disease or health status

## 🔧 Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 128x128 pixels
- **Output**: 38-class classification
- **Training**: Transfer learning with data augmentation

## 📈 Performance

The model achieves high accuracy across multiple plant disease categories, making it suitable for real-world agricultural applications.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset source: Plant Disease Recognition Dataset
- Streamlit for the web framework
- TensorFlow/Keras for the deep learning framework

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Note**: This application is for educational and research purposes. For commercial agricultural applications, please consult with agricultural experts. 