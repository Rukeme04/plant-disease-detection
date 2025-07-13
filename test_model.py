import tensorflow as tf
import os

print("TensorFlow version:", tf.__version__)
print("Current directory:", os.getcwd())
print("Files in directory:", [f for f in os.listdir('.') if 'model' in f.lower()])

# Try loading H5 model
try:
    print("\nTrying to load trained_model.h5...")
    model_h5 = tf.keras.models.load_model('trained_model.h5')
    print("✓ H5 model loaded successfully!")
except Exception as e:
    print(f"✗ Error loading H5 model: {e}")

# Try loading Keras model
try:
    print("\nTrying to load trained_model.keras...")
    model_keras = tf.keras.models.load_model('trained_model.keras')
    print("✓ Keras model loaded successfully!")
except Exception as e:
    print(f"✗ Error loading Keras model: {e}") 